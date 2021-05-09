from twilio.rest import Client
import os
import smtplib

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_email = os.environ["EMAIL"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    def send_message(self, text):
        message = self.client.messages.create(
            body= text,
            from_=os.environ['TWILIO_PHONE_NUMBER'],
            to=os.environ['PHONE_NUMBER']
        )
        print(message.status)

    def send_emails(self, emails, text, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=os.environ["PASSWORD"])
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs= email,
                    msg=f"Subject:New Low Price Flight!\n\n{text}\n{google_flight_link}".encode('utf-8'),
                )