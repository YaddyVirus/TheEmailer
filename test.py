import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time
import schedule
from twilio.rest import Client

client = Client("Twilio Acc no","Twilio Auth key")
check = time.strftime("%a")
i= datetime.datetime.now()
fromaddr = "my email"
toaddr = "reciever's email"
dmy = str(i.day)+"/"+str(i.month)+"/"+str(i.year)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Attendance for Yadullah Abidi for "+dmy #the dmy variable has the curret date for the day in a string format

if (check == "Fri" or check =="Mon"): #Monday and friday I have to go to a different place than my usual office.
    body = "Good morning.\nI reached Ardee School at 9:15 AM today."
else:
    body = "Good morning.\nI reached MakersBox Okhla at 10:00 AM today."

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password to gmail")
text = msg.as_string()
def mail():
    server.sendmail(fromaddr, toaddr, text)
    client.messages.create(to="My phone number",from_="Twilio phone number",body="Attendance mail sent")
    print("Sent")

if (check == "Fri" or check =="Mon"):
    schedule.every().day.at("09:10").do(mail)
elif(check == "Sun"):
    print("Have a nice holiday!")
else:
    schedule.every().day.at("09:55").do(mail)

while True:
    schedule.run_pending()
    time.sleep(1)
