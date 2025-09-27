# 🚗 GestureDrive: Car Game Control Using Hand Gestures 👋

## 📖 Overview
**GestureDrive** is an innovative project that allows you to control a car game using hand gestures! 🎮 By leveraging computer vision and gesture recognition, this system captures hand movements via a webcam and translates them into keyboard inputs to control the car in real-time. Whether you're turning left, turning right, moving forward, or reversing, GestureDrive makes gaming more interactive and fun! 🖐️
## ✨ Features
- **Real-Time Hand Tracking**: Uses **Mediapipe Hands** to detect and track hand landmarks in real-time. 👋
- **Gesture Recognition**: Recognizes specific hand gestures to control the car (e.g., turn left, turn right, move forward, reverse). 🚦
- **Keyboard Input Simulation**: Simulates keyboard inputs (`w`, `a`, `s`, `d`) to control the car in the game. ⌨️
- **Visual Feedback**: Displays hand landmarks and gestures on the screen with real-time visual feedback. 🎥
- **Easy to Use**: Just wave your hands in front of the camera to control the car! 🖐️


## 🛠️ Requirements
To run this project, you need the following Python libraries installed:

- `opencv-python`
- `mediapipe`
- `math`
- `keyinput` (custom module for simulating keyboard inputs)

## Perform Hand Gestures:

Turn Left: Gesture to turn left. ⬅️

Turn Right: Gesture to turn right. ➡️

Move Forward: Gesture to move forward. ⬆️

Move Backward: Gesture to move backward. ⬇️

Press q to Quit: Exit the application anytime by pressing the q key. ❌

## 🗂️ Code Structure
car.py: The main script that captures video, processes hand gestures, and simulates keyboard inputs.

keyinput.py: A custom module for simulating keyboard inputs.


## You can install the required libraries using pip:
```bash
pip install opencv-python mediapipe
git clone https://github.com/Syam-1133/Car-Game-Control-Using-Hand-Gestures-
python car.py


