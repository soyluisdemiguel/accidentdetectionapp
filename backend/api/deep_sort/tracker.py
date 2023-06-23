from collections import deque
from deep_sort.kalman_filter import KalmanFilter

class Track:
    def __init__(self, mean, covariance, track_id):
        self.mean = mean
        self.covariance = covariance
        self.track_id = track_id
        self.hits = 1
        self.age = 1
        self.time_since_update = 0

    def predict(self, kf):
        self.mean, self.covariance = kf.predict(self.mean, self.covariance)
        self.age += 1
        self.time_since_update += 1

    def update(self, kf, detection):
        self.mean, self.covariance = kf.update(self.mean, self.covariance, detection.to_xyah())
        self.hits += 1
        self.time_since_update = 0

    def mark_missed(self):
        self.age += 1
        self.time_since_update += 1

    def is_tentative(self):
        return self.hits <= 1

    def is_confirmed(self):
        return self.hits > 1
        
        
class Tracker:
    
def init(self, metric, max_age, n_init):
self.metric = metric
self.max_age = max_age
self.n_init = n_init
self.kf = KalmanFilter()
self.tracks = []
self._next_id = 1

def predict(self):
    for track in self.tracks:
        track.predict(self.kf)

def update(self, detections):
    matches, unmatched_tracks, unmatched_detections = self._match(detections)

    for track_idx, detection_idx in matches:
        self.tracks[track_idx].update(self.kf, detections[detection_idx])

    for track_idx in unmatched_tracks:
        self.tracks[track_idx].mark_missed()

    for detection_idx in unmatched_detections:
        self._initiate_track(detections[detection_idx])

    self.tracks = [t for t in self.tracks if not t.is_deleted()]

def _match(self, detections):
    confirmed_tracks = [i for i, t in enumerate(self.tracks) if t.is_confirmed()]
    unconfirmed_tracks = [i for i, t in enumerate(self.tracks) if t.is_tentative()]

    matches_a, unmatched_tracks_a, unmatched_detections = self.metric.match(
        [self.tracks[i] for i in confirmed_tracks],
        detections
    )
    matches_a = [(confirmed_tracks[i], j) for i, j in matches_a]

    matches_b, unmatched_tracks_b, unmatched_detections = self.metric.match(
        [self.tracks[i] for i in unconfirmed_tracks],
        [detections[i] for i in unmatched_detections]
    )
    matches_b = [(unconfirmed_tracks[i], j) for i, j in matches_b]

    unmatched_tracks = list(set(unmatched_tracks_a) | set(unmatched_tracks_b))
    matches = matches_a + matches_b
    return matches, unmatched_tracks, unmatched_detections

def _initiate_track(self, detection):
    mean, covariance = self.kf.initiate(detection.to_xyah())
    self.tracks.append(Track(mean, covariance, self._next_id))
    self._next_id += 1
