from fastapi import APIRouter
from api.mobile_app_communication import MobileAppCommunication

router = APIRouter()

mobile_app_communication = MobileAppCommunication()

@router.post("/emergency_alerts")
async def send_emergency_alert(alert_data: dict):
    # Send alert to the mobile app
    mobile_app_communication.send_alert_to_mobile_app(alert_data)
    
    # Update central alert system
    update_central_alert_system(alert_data)
    
    return {"message": "Emergency alert sent"}

def update_central_alert_system(alert_data):
    # Code to update the central alert system with the received alert_data
    pass
