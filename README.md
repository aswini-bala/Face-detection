**Real-Time Face Detection with OpenCV and cvzone**

This project demonstrates real-time face detection using a webcam feed. The application uses OpenCV for video capture and the FaceDetectionModule from cvzone for detecting faces.

**Features**
    Real-time face detection from a webcam.
    Bounding boxes drawn around detected faces.
    Easy to exit with a keypress ('q').

**Requirements**
Before running the project, ensure you have installed the following dependencies:
        Python 3.x
        OpenCV
        cvzone

**Install the dependencies**

Use pip to install the required libraries:

Code:
pip install opencv-python cvzone

**How to Run**
    Clone or download this repository to your local machine.
    Navigate to the project directory in your terminal.
    Run the Python script

**Code Explanation**

**1. Import Libraries**
    The script starts by importing the necessary libraries. OpenCV (cv2) is used for capturing video from the webcam, and cvzone.FaceDetectionModule provides an easy-to-use interface for face detection.
**2. Initialize Webcam and Face Detector**
   The webcam is accessed using cv2.VideoCapture(0) where 0 is the index for the default webcam.
    A face detector object is created using FaceDetector() from cvzone.
**3. Face Detection in Real-Time**
    The while True loop reads the frames from the webcam and passes them to the face detector. The bounding boxes (bbox) are drawn around detected faces.
**4. Display and Exit**
    The detected faces are displayed in a window. Press 'q' to exit the application gracefully.
