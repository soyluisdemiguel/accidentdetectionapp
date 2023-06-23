import requests

class MobileAppCommunication:
    def __init__(self):
        self.mobile_app_base_url = "https://example.com/mobile_app_api"  # Replace with the mobile app API URL

    def send_alert_to_mobile_app(self, alert_data):
        url = f"{self.mobile_app_base_url}/send_alert"
        response = requests.post(url, json=alert_data)

        if response.status_code == 200:
            print("Alert sent to mobile app")
        else:
            print(f"Failed to send alert to mobile app: {response.text}")
