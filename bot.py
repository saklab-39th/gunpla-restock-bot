import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1468905881025642496/Nz9PcITWPC6K7gDG95A0mrqkKaqKnbqXHvs-yxDEW01k5gxKBNHv_d_oNTPwcQDbLbfG"
URL = "https://p-bandai.jp/item/item-1000135894/"

html = requests.get(URL).text

def notify(text):
    requests.post(WEBHOOK_URL, json={"content": text})

if "再販受付中" in html:
    notify("🎉 ガンプラ再販！『再販受付中』になりました")

elif "予約受付中" in html:
    notify("🎉 ガンプラ再販！『予約受付中』になりました")

elif "販売中" in html:
    notify("🎉 ガンプラ販売中になりました")

else:
    print("まだ再販されていません")
