import cv2
import numpy as np
from tensorflow.keras.models import load_model

class RealTimeObjectDetection:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = load_model(model_path)
        self.input_shape = self.model.layers[0].input_shape[1:3]

    def process_frame(self, frame):
        resized_frame = cv2.resize(frame, self.input_shape)
        input_data = np.expand_dims(resized_frame, axis=0)
        predictions = self.model.predict(input_data)
        return predictions

    def start_detection(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        while True:
            ret, frame = cap.read()
            predictions = self.process_frame(frame)
            # Do something with the predictions
            # ...
            # Display the resulting frame
            cv2.imshow('Real-time object detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    model_path = "path/to/object_detection_model.h5"
    detector = RealTimeObjectDetection(model_path)
    detector.start_detection()
