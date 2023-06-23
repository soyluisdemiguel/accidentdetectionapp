class HardwareConfig:
    def __init__(self):
        self.camera = {
            'resolution': (640, 480),
            'fps': 30,
        }

    def get_camera_config(self):
        return self.camera
