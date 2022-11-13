import schedule
import cowinEmail

try:
    schedule.every(5).minutes.do(cowinEmail.sendEmail())
    print("SENT!")
except:
    print("ERROR")


while True:
    schedule.run_pending()