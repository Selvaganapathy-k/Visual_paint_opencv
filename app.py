import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("🎨 Visual Paint - Streamlit Version")

# HSV range for blue object
HSV_RANGE = [90, 70, 70, 115, 255, 255]
DRAW_COLOR = (210, 180, 140)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        global canvas

        img = frame.to_ndarray(format="bgr24")
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower = np.array(HSV_RANGE[:3])
        upper = np.array(HSV_RANGE[3:6])

        mask = cv2.inRange(imgHSV, lower, upper)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 1500:
                x, y, w, h = cv2.boundingRect(largest)
                cx = x + w // 2
                cy = y + h // 2
                cv2.circle(canvas, (cx, cy), 8, DRAW_COLOR, cv2.FILLED)

        result = cv2.add(img, canvas)
        return result


webrtc_streamer(key="paint", video_transformer_factory=VideoTransformer)

if st.button("Clear Canvas"):
    canvas[:] = 0
