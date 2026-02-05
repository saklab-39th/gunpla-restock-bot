import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1468905881025642496/Nz9PcITWPC6K7gDG95A0mrqkKaqKnbqXHvs-yxDEW01k5gxKBNHv_d_oNTPwcQDbLbfG"
URL = "https://p-bandai.jp/item/item-1000135894/"

html = requests.get(URL).text

# ページの中身を少しだけ表示（デバッグ用）
print(html[:500])

if "再販受付中" in html:
    print("再販受付中 を見つけました！")

elif "予約受付中" in html:
    print("予約受付中 を見つけました！")

elif "販売中" in html:
    print("販売中 を見つけました！")

else:
    print("まだ再販されていません")
