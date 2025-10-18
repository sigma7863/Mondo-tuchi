from win11toast import toast
import schedule, time

print("実行中")
# 通知バナー表示させて、クリックするとMondoのサイトに飛ぶ
def url_open():
    toast(
    "Mondo",
    "Mondoの時間です!",
    on_click="https://mondo.quizknock.com/"
    )
    
# 毎日0:00になると実行
    schedule.every().day.at("00:00").do(url_open) 
    while True:
        schedule.run_pending()
        time.sleep(1)
