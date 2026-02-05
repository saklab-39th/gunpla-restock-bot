import requests
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/1468905881025642496/Nz9PcITWPC6K7gDG95A0mrqkKaqKnbqXHvs-yxDEW01k5gxKBNHv_d_oNTPwcQDbLbfG"
URL = "https://p-bandai.jp/item/item-1000135894/"

STATUS_FILE = "status.txt"

def notify(text):
    requests.post(WEBHOOK_URL, json={"content": text})

# 前回の状態を読む
if os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, "r") as f:
        last_status = f.read().strip()
else:
    last_status = "NOT_AVAILABLE"

html = requests.get(URL).text

# 今回の状態を判定
if "再販受付中" in html or "予約受付中" in html or "販売中" in html:
    current_status = "AVAILABLE"
else:
    current_status = "NOT_AVAILABLE"

# 状態が変わった瞬間だけ通知
if last_status == "NOT_AVAILABLE" and current_status == "AVAILABLE":
    notify("🎉 ガンプラ再販されました！今すぐ確認してください！")

# 状態を保存
with open(STATUS_FILE, "w") as f:
    f.write(current_status)
