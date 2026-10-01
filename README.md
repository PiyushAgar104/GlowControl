# Finger Brightness Control 🖐️

A computer vision project that allows you to control your system screen brightness using hand gestures through a webcam.

## 🚀 Features

* Real-time hand detection using MediaPipe
* Thumb and index finger tracking
* Finger distance mapped to screen brightness
* Live brightness percentage display
* Works with a normal webcam
* Simple and lightweight Python implementation

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* Screen Brightness Control

## 📂 Project Structure

```text
Finger-Brightness-Control/
│
├── brightness_control.py
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd Finger-Brightness-Control
```

Install the required libraries:

```bash
pip install opencv-python mediapipe screen-brightness-control
```

## ▶️ Run the Project

```bash
python brightness_control.py
```

Allow camera access when prompted.

## 🖐️ How It Works

```text
Webcam
   ↓
Hand Detection
   ↓
Thumb + Index Finger Tracking
   ↓
Calculate Finger Distance
   ↓
Map Distance to Brightness
   ↓
Change System Brightness
```

### Gesture Control

| Gesture           | Brightness |
| ----------------- | ---------- |
| Fingers close 🤏  | Low        |
| Fingers apart 🖐️ | High       |

The distance between the thumb and index finger is continuously calculated and converted into a brightness percentage from **0% to 100%**.

## 🎯 Controls

Press **Q** to exit the application.

## 📌 Requirements

* Python 3.10+
* Webcam
* Windows system with supported brightness control

## 🔮 Future Improvements

* Smooth brightness transitions
* Gesture-based volume control
* Multiple hand gesture commands
* Custom brightness sensitivity
* GUI-based controls
* Cross-platform support

## 👨‍💻 Author

**Piyush Agar**

B.Tech AI & Data Science
Poornima University, Jaipur

---

⭐ If you find this project useful, consider giving the repository a star!
