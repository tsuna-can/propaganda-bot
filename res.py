
#曲登録時のダイアログ
modal = {
	"type": "modal",
    "callback_id": "modal-id",
	"title": {
		"type": "plain_text",
		"text": "曲の登録",
		"emoji": False
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": False
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": False
	},
	"blocks": [
		{
			"type": "divider"
		},
		{
			"type": "input",
			"block_id": "b-id0",
			"element": {
				"type": "plain_text_input",
				"action_id": "id_song_name",
				"placeholder": {
					"type": "plain_text",
					"text": "曲名",
					"emoji": False
				}
			},
			"label": {
				"type": "plain_text",
				"text": "曲名",
				"emoji": False
			}
		},
		{
			"type": "input",
			"block_id": "b-id1",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "id_comment",
				"placeholder": {
					"type": "plain_text",
					"text": "コンフント名とか推しポイントとか",
					"emoji": False
				}
			},
			"label": {
				"type": "plain_text",
				"text": "コメント",
				"emoji": False
			}
		},
		{
			"type": "input",
			"block_id": "b-id2",
			"element": {
				"type": "plain_text_input",
				"action_id": "id_url",
				"placeholder": {
					"type": "plain_text",
					"text": "あれば動画のURLなど",
					"emoji": False
				}
			},
			"label": {
				"type": "plain_text",
				"text": "URL",
				"emoji": False
			},
			"optional": True
		},
		{
			"type": "input",
			"block_id": "b-id3",
			"element": {
				"type": "plain_text_input",
				"action_id": "id_tourokusya",
				"placeholder": {
					"type": "plain_text",
					"text": "名無しの宣教師",
					"emoji": False
				}
			},
			"label": {
				"type": "plain_text",
				"text": "登録者",
				"emoji": False
			},
			"optional": True
		}
	]
}