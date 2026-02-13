🎨 Visual Paint Web App (Streamlit + OpenCV)

A real-time color detection drawing web application built using OpenCV, Streamlit, and WebRTC.

This application allows users to draw on screen using a colored object detected via webcam directly inside the browser.

🌐 Live Demo

👉 Try the App Here:
https://visualpaintopencv-selva.streamlit.app/

🚀 Features

🎥 Real-time webcam streaming in browser

🎯 HSV-based color detection

🧹 Noise removal using morphological operations

🖌️ Virtual canvas drawing

🔄 Clear canvas button

🌐 Fully browser-based (no local OpenCV window)

🛠 Tech Stack

Python

OpenCV

NumPy

Streamlit

streamlit-webrtc

📂 Project Structure
visual-paint/
│
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md

⚙️ Run Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/visual-paint.git
cd visual-paint

2️⃣ Create Virtual Environment
python -m venv venv


Activate (Windows):

venv\Scripts\activate


Activate (Mac/Linux):

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

🎮 How It Works

Webcam feed captured via WebRTC

Frame converted to HSV color space

Selected color detected using thresholding

Morphological operations remove noise

Largest contour detected

Center point drawn onto virtual canvas

Canvas merged with live frame

📌 Future Improvements

🎨 Add multiple color selection

🖌️ Brush thickness slider

💾 Save drawing as image

📷 Screenshot feature

📊 Live HSV tuning controls

👨‍💻 Author

Selvaganapathy K