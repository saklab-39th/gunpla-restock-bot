import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1468905881025642496/Nz9PcITWPC6K7gDG95A0mrqkKaqKnbqXHvs-yxDEW01k5gxKBNHv_d_oNTPwcQDbLbfG"

message = {
    "content": "🤖 Botのテスト通知です。正常に動いています。"
}

requests.post(WEBHOOK_URL, json=message)
