import smtplib
import cowinAPI
from decouple import config

GMAIL_USER = config('GMAIL_USER')
GMAIL_PASSWORD = config('GMAIL_PASSWORD')

SUBJECT = 'CoWIN Vaccine Updates'

sentFrom = GMAIL_USER
to = ['paulamixbhattacharya@gmail.com']

# District ID's
# Hyderabad - 581
# Rangareddy - 603

def getEmailBody(districtID, date, districtName):
    return "------------- " + districtName + " ---------------\n\n" + str(cowinAPI.parseResponse(districtID, date)) + "\n"


body = getEmailBody('603', '28-05-2021', 'RANGAREDDY DISTRICT') + getEmailBody('581', '28-05-2021', 'HYDERABAD DISTRICT')

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sentFrom, ", ".join(to), SUBJECT, body)


def sendEmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(sentFrom, to, email_text)
    server.close()

try:
    sendEmail()
    print("SENT!")
except:
    print("ERROR!")
