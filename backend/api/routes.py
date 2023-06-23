from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from .accident_detection import AccidentDetection
import cv2
import base64

router = APIRouter()  # Create an APIRouter instance

class Frame(BaseModel):
    image: str

# Comment out the line that creates the AccidentDetection instance
# accident_detector = AccidentDetection("path/to/accident_detection_model.h5")

@router.post("/detect-accident", response_model=float)
async def detect_accident(frame: Frame) -> float:
    try:
        # image_data = base64.b64decode(frame.image)
        # np_arr = np.frombuffer(image_data, np.uint8)
        # decoded_frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Comment out the line that runs the actual detection process
        # accident_probability = accident_detector.detect_accident(decoded_frame)
        
        # Return a dummy value instead
        accident_probability = 0.0
        return accident_probability
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
