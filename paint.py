import cv2
import numpy as np

# ==============================
# Camera Settings
# ==============================
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

# ==============================
# HSV Range (Blue detection only)
# ==============================
# Adjust if needed for your lighting
myColors = [
    [90, 70, 70, 115, 255, 255]   # Blue object range
]

# ==============================
# Drawing Color (Pastel Blue)
# ==============================
myColorValues = [
    (210, 180, 140)
]

# ==============================
# Canvas
# ==============================
canvas = np.zeros((frameHeight, frameWidth, 3), dtype=np.uint8)

# ==============================
# Function to Get Center (Improved)
# ==============================
def getCenter(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None

    # Take largest contour only
    largest = max(contours, key=cv2.contourArea)

    if cv2.contourArea(largest) > 1500:   # Increase if noise still appears
        x, y, w, h = cv2.boundingRect(largest)
        cx = x + w // 2
        cy = y + h // 2
        return cx, cy

    return None

# ==============================
# Main Loop
# ==============================
while True:
    success, img = cap.read()
    if not success:
        print("Camera not accessible.")
        break

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i, color in enumerate(myColors):
        lower = np.array(color[:3])
        upper = np.array(color[3:6])

        mask = cv2.inRange(imgHSV, lower, upper)

        # ---------- Noise Removal ----------
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        center = getCenter(mask)

        if center is not None:
            cv2.circle(canvas, center, 8, myColorValues[i], cv2.FILLED)

    # Combine camera + drawing
    result = cv2.add(img, canvas)

    cv2.imshow("Visual Paint", result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):   # Quit
        break
    elif key == ord('c'): # Clear canvas
        canvas[:] = 0

# ==============================
# Cleanup
# ==============================
cap.release()
cv2.destroyAllWindows()
