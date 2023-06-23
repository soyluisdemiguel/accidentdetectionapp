import os
import tensorflow as tf

class IAModels:
    def __init__(self):
        self.model_paths = {
            'accident_detection': 'path/to/accident_detection_model.h5',
        }

    def load_model(self, model_name):
        if model_name in self.model_paths:
            model_path = self.model_paths[model_name]
            if os.path.exists(model_path):
                return tf.keras.models.load_model(model_path)
            else:
                raise Exception(f"Model file not found: {model_path}")
        else:
            raise Exception(f"Model not found: {model_name}")

    def get_model(self, model_name):
        return self.load_model(model_name)
