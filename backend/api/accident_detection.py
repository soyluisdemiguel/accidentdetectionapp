import numpy as np
import cv2
from tensorflow.keras.models import load_model

class AccidentDetection:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.input_shape = self.model.layers[0].input_shape[1:3]

    def preprocess_frame(self, frame):
        resized_frame = cv2.resize(frame, self.input_shape)
        normalized_frame = resized_frame / 255.0
        return np.expand_dims(normalized_frame, axis=0)

    def detect_accident(self, frame):
        preprocessed_frame = self.preprocess_frame(frame)
        prediction = self.model.predict(preprocessed_frame)
        return prediction[0][0]

if __name__ == "__main__":
    model_path = "path/to/accident_detection_model.h5"
    accident_detector = AccidentDetection(model_path)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        accident_probability = accident_detector.detect_accident(frame)
        if accident_probability > 0.5:
            print("Accident detected with probability:", accident_probability)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
