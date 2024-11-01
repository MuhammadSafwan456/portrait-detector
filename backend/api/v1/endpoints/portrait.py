# Third Party Imports
import cv2
import numpy as np
from fastapi import APIRouter, File, HTTPException, UploadFile

# Local Imports
from api.v1 import responses
from api.v1.utils import extract_portrait

router = APIRouter()


@router.post("/extract/", responses=responses.portrait["extract"])
async def extract(
    image: UploadFile = File(...),
):
    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="File format not supported")

    image_bytes = await image.read()
    np_array = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    base64_image = extract_portrait(image)
    if image is None:
        raise HTTPException(status_code=400, detail="Could not process the image")
    return {"image": base64_image}
