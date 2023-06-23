class NotificationCustomization:
    def __init__(self, user):
        self.user = user
        self.preferences = {
            "silent_hours": (22, 7),
            "geofence": None,
            "event_types": {"accident", "traffic_jam", "road_closure"},
        }

    def set_silent_hours(self, start_hour, end_hour):
        self.preferences["silent_hours"] = (start_hour, end_hour)

    def set_geofence(self, geofence):
        self.preferences["geofence"] = geofence

    def set_event_types(self, event_types):
        self.preferences["event_types"] = set(event_types)

    def should_notify(self, event):
        if event["type"] not in self.preferences["event_types"]:
            return False

        if self.preferences["geofence"] and not self.preferences["geofence"].contains(event["location"]):
            return False

        current_hour = datetime.datetime.now().hour
        silent_start, silent_end = self.preferences["silent_hours"]
        if silent_start < silent_end:
            if silent_start <= current_hour < silent_end:
                return False
        else:
            if not (silent_end <= current_hour < silent_start):
                return False

        return True
