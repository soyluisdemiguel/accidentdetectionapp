import smtplib
from email.message import EmailMessage

class EmailEmergencyContact:
    def __init__(self, email_address, smtp_server, smtp_port, smtp_user, smtp_password):
        self.email_address = email_address
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_notification(self, message):
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = "Emergency Assistance Request"
        msg["From"] = self.smtp_user
        msg["To"] = self.email_address

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)

class SmsEmergencyContact:
    def __init__(self, phone_number, sms_gateway_api_key, sms_gateway_url):
        self.phone_number = phone_number
        self.sms_gateway_api_key = sms_gateway_api_key
        self.sms_gateway_url = sms_gateway_url

    def send_notification(self, message):
        payload = {
            "api_key": self.sms_gateway_api_key,
            "phone_number": self.phone_number,
            "message": message
        }
        response = requests.post(self.sms_gateway_url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")
