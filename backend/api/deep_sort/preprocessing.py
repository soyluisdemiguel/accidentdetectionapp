import cv2
import numpy as np
from deep_sort.encoder import create_box_encoder

def create_box_encoder(model_filename, input_name="images", output_name="features", batch_size=32):
    encoder = create_box_encoder(model_filename, batch_size)
    return lambda image, boxes: encoder(image, boxes)

def non_max_suppression(boxes, max_bbox_overlap, scores=None):
    if len(boxes) == 0:
        return []

    boxes = boxes.astype(np.float)
    pick = []

    x1, y1, x2, y2 = boxes.T
    area = (x2 - x1 + 1) * (y2 - y1 + 1)

    if scores is not None:
        idxs = scores.argsort()[::-1]
    else:
        idxs = np.argsort(y2)

    while len(idxs) > 0:
        i = idxs[0]
        pick.append(i)
        idxs = idxs[1:]

        xx1 = np.maximum(x1[i], x1[idxs])
        yy1 = np.maximum(y1[i], y1[idxs])
        xx2 = np.minimum(x2[i], x2[idxs])
        yy2 = np.minimum(y2[i], y2[idxs])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs]
        idxs = idxs[overlap <= max_bbox_overlap]

    return pick
