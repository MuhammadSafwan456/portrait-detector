# Standard Library Imports
import base64

# Third Party Imports
import cv2
from fastapi import HTTPException


def extract_portrait(image):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        raise HTTPException(status_code=400, detail="No face detected in the image")

    x, y, w, h = faces[0]

    portrait = image[y : y + h, x : x + w]  # noqa E203
    _, buffer = cv2.imencode(".jpg", portrait)
    base64_image = base64.b64encode(buffer).decode("utf-8")
    html_img_tag = (
        f'<img src="data:image/jpeg;base64,{base64_image}" alt="Base64 Image">'
    )
    print(html_img_tag)
    return base64_image
