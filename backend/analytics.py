# AccidentDetectionApp/backend/analytics.py

import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Analytics:
    def __init__(self):
        self.events = []

    def log_event(self, event_type, event_data):
        event = {
            "timestamp": datetime.utcnow(),
            "event_type": event_type,
            "event_data": event_data,
        }
        self.events.append(event)
        logger.info(f"Logged event: {event}")

    def get_events(self, event_type=None):
        if event_type:
            return [event for event in self.events if event["event_type"] == event_type]
        else:
            return self.events

if __name__ == "__main__":
    analytics = Analytics()
    analytics.log_event("user_login", {"username": "john_doe"})
    analytics.log_event("user_logout", {"username": "john_doe"})
    print(analytics.get_events())
