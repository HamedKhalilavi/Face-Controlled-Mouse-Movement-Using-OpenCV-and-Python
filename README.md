# Face Mouse Controller

#### Video Demo: [YouTube Video Link Here]

#### Description:

Face Mouse Controller is a Python-based computer vision project that allows a user to control the mouse cursor using their facial position. By leveraging OpenCV’s Haar cascade classifiers to detect the position of the user's face and eyes in real-time from webcam input, the system moves the mouse cursor accordingly to simulate head-based navigation. This project is particularly useful for accessibility purposes, enabling basic mouse control for individuals with limited mobility.

The system uses the `pyautogui` library to move the mouse pointer based on the face's horizontal and vertical displacement from a predefined bounding box. When the user’s face moves outside this region, the pointer shifts in the corresponding direction. Additionally, the program provides live visual feedback by drawing rectangles around the detected face and eyes on the screen.

---

### Features

- Real-time face and eye detection using OpenCV Haar cascades  
- Live video feed display with overlay rectangles  
- Detection of face position relative to a center box  
- Automatic mouse movement based on head motion  
- Visual color cues when movement is triggered (red border)  
- Works with any standard webcam  
- Hands-free interaction with system mouse

---

### Project Files

- **`main.py`**: The main Python script that captures webcam input, detects facial and eye positions, and controls the mouse using `pyautogui`.
- **`README.md`**: This documentation file describing the project, functionality, design decisions, and setup instructions.
- **`haarcascade_frontalface_default.xml`**: A pre-trained Haar cascade XML model file from OpenCV used for detecting frontal human faces.
- **`haarcascade_eye.xml`**: A pre-trained Haar cascade XML model file used for detecting human eyes within a detected face region.

---

### How It Works

1. **Initialization**:  
   The webcam is activated using `cv2.VideoCapture(0)`, and the screen resolution is detected using `pyautogui.size()`.

2. **Model Loading**:  
   The system loads two Haar cascade models from OpenCV’s built-in directory:
   - `haarcascade_frontalface_default.xml` – detects frontal faces in the camera frame.
   - `haarcascade_eye.xml` – detects eyes within the face region.

3. **Frame Processing**:
   - Each captured frame is flipped horizontally and converted to grayscale.
   - The face detection model locates any visible faces.
   - If a face is found, a rectangle is drawn, and a subregion is used for eye detection.
   - When the face moves out of a predefined bounding box (200,100)-(450,350), the mouse moves in that direction using `pyautogui.moveTo()`.
   - The eye model detects up to two eyes for visualization and confirmation.

4. **Exit Condition**:  
   Pressing the `q` key terminates the loop, releases the camera, and closes all OpenCV windows.

---

### Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- PyAutoGUI (`pyautogui`)
- NumPy (`numpy`)
- Webcam
- Haar cascade model files (included with OpenCV):
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

Install dependencies with:

```bash
pip install opencv-python pyautogui numpy
