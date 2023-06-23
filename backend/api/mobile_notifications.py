from twilio.rest import Client


class MobileNotifications:
    def __init__(self, account_sid, auth_token, twilio_phone_number):
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_sms(self, to, body):
        self.client.messages.create(body=body, from_=self.twilio_phone_number, to=to)
