import os
import json
import random
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from slack_sdk.errors import SlackApiError
from flask import Flask, request, make_response
from entities.sql_settings import session
from entities.sql_settings import SongList
from res import modal


SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SIGNATURE_VERIFIER = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])
client = WebClient(token=SLACK_TOKEN)
app = Flask(__name__)


"""
メイン部分
"""
@app.route("/slack/events", methods=["GET", "POST"])
def slack_app():
    if not SIGNATURE_VERIFIER.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)

    req = request.form

    #登録コマンド
    if "/touroku" == req.get("command"):
        try:
            api_response = client.views_open(
                trigger_id = req.get("trigger_id"),
                view = modal
            )
            return make_response("", 200)
        except SlackApiError as e:
            code = e.response["error"]
            return make_response(f"Failed to open a modal due to {code}", 200)
    
    #呼び出しコマンド
    if "/hukyo" == req.get("command"):
        try:
            #曲の選択
            data = session.query(SongList).filter(SongList.num_hukyo==0).first()
            if not data:
                rowCount = session.query(SongList).count()
                tmp_id = random.randint(1, rowCount)
                data = session.query(SongList).filter(SongList.id == tmp_id).first()
            
            tmp_id = data.id
            tmp_hukyo = data.num_hukyo + 1

            api_response = client.chat_postMessage(
                channel='propaganda_channel',
                text = ">>>" +  "【曲名】\n" + str(data.song_name) +  \
                                "\n【コメント】\n" + str(data.comments) + \
                                "\n\nURL：" + str(data.url) + \
                                "\n\n登録者：" + str(data.tourokusya) + "　布教回数：" + str(tmp_hukyo)
            )

            #データの更新
            selected_song = session.query(SongList).filter(SongList.id == tmp_id).first()
            selected_song.num_hukyo = tmp_hukyo
            session.commit()

            return make_response("", 200)

        except SlackApiError as e:
            code = e.response["error"]
            return make_response(f"Failed to open a modal due to {code}", 200)

    
    #曲登録ダイアログを受け取った時
    if "payload" in request.form:
        payload = json.loads(request.form["payload"])

        if payload["type"] == "view_submission" and payload["view"]["callback_id"] == "modal-id":
            submitted_data =  payload["view"]["state"]["values"]
            song = submitted_data["b-id0"]["id_song_name"]["value"]
            comment = submitted_data["b-id1"]["id_comment"]["value"]
            movie_url = submitted_data["b-id2"]["id_url"]["value"]
            tourokusya = submitted_data["b-id3"]["id_tourokusya"]["value"]

            new_song = SongList(song_name=song, comments=comment, url=movie_url, tourokusya=tourokusya, num_hukyo=0)
            session.add(instance=new_song)
            session.commit()

            api_response = client.chat_postMessage(
                channel='#propaganda_channel',
                text = "登録されました"
            )

            return make_response("", 200)

    return make_response("", 404)

#localで動かすとき
if __name__ == "__main__":
    app.run("localhost", 3000)


