import cv2
import numpy as np
from deep_sort import preprocessing
from deep_sort import nn_matching
from deep_sort.tracker import Tracker
from deep_sort.detection import Detection
from yolov3.yolo import YOLOv3

class AccidentDetectionIA:
    def __init__(self, yolov3_weights, deep_sort_weights):
        self.yolo = YOLOv3(yolov3_weights)
        self.deep_sort_metric = nn_matching.NearestNeighborDistanceMetric("cosine", 0.2, None)
        self.deep_sort_tracker = Tracker(self.deep_sort_metric, max_age=30, n_init=3)
        self.deep_sort_encoder = preprocessing.create_box_encoder(deep_sort_weights, batch_size=32)

    def process_frame(self, frame):
        detections = self.detect_objects(frame)
        tracker = self.track_objects(frame, detections)
        self.analyze_trajectories(tracker.tracks)
        self.draw_results(frame, tracker.tracks)
        return frame

    def detect_objects(self, frame):
        detections = self.yolo.detect(frame)
        return [Detection(box[:4], box[4]) for box in detections]

    def track_objects(self, frame, detections):
        features = self.deep_sort_encoder(frame, [d.tlwh for d in detections])
        detections = [Detection(d.tlwh, d.confidence, feat) for d, feat in zip(detections, features)]
        self.deep_sort_tracker.predict()
        self.deep_sort_tracker.update(detections)
        return self.deep_sort_tracker

    def analyze_trajectories(self, tracks):
# Analizar las trayectorias de los objetos rastreados para detectar posibles accidentes
        for track in tracks:
            if track.is_confirmed() and track.time_since_update == 0:
                self.check_for_accidents(track)

    def check_for_accidents(self, track):
        # Aquí puedes implementar la lógica para verificar si un objeto rastreado está involucrado en un accidente
        # Puedes considerar factores como la velocidad, la dirección y el tipo de objeto rastreado
        # Si se detecta un accidente, puedes activar una notificación o alerta en tiempo real
        pass

    def draw_results(self, frame, tracks):
        # Dibuja los resultados de la detección y el seguimiento en el frame
        for track in tracks:
            if track.is_confirmed() and track.time_since_update == 0:
                box = track.to_tlwh()
                x, y, w, h = map(int, box)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f"ID: {track.track_id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

if __name__ == "__main__":
    yolov3_weights = "path/to/yolov3.weights"
    deep_sort_weights = "path/to/mars-small128.pb"
    video_path = "path/to/video.mp4"
    output_path = "path/to/output.mp4"

    detector = AccidentDetectionIA(yolov3_weights, deep_sort_weights)

    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = detector.process_frame(frame)
        out.write(processed_frame)
        cv2.imshow("Frame", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
