🎨 Visual Paint Web App (Streamlit + OpenCV)

A real-time color detection drawing web application built using OpenCV, Streamlit, and WebRTC.

This application allows users to draw on screen using a colored object detected via webcam directly inside the browser.

🚀 Live Features

🎥 Real-time webcam streaming in browser

🎯 HSV-based color detection

🧹 Noise removal using morphological operations

🖌️ Virtual canvas drawing

🔄 Clear canvas button

🌐 Browser-based interface (no cv2.imshow() window)

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
└── README.md

⚙️ Installation (Local Setup)
1️⃣ Clone Repository
git clone https://github.com/your-username/visual-paint.git
cd visual-paint

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate (Windows):

venv\Scripts\activate


Activate (Mac/Linux):

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py


The app will open automatically in your browser.

🌍 Deploy Online (Streamlit Cloud)

Push project to GitHub

Go to https://streamlit.io/cloud

Connect your GitHub account

Select this repository

Click Deploy

Your app will be live online.

🎮 How It Works

Webcam feed captured via WebRTC

Frame converted to HSV color space

Selected color detected using thresholding

Morphological operations remove noise

Largest contour detected

Center point drawn onto virtual canvas

Canvas merged with live frame

📌 Future Improvements

🎨 Color selection dropdown

🖌️ Brush thickness control

💾 Save drawing as image

📷 Screenshot capture

📊 Add UI controls for HSV tuning

👨‍💻 Author

Selvaganapathy K