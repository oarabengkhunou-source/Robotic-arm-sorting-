🤖 Robotic Arm Sorting System

A Raspberry Pi Pico-based robotic arm designed to identify and sort recyclable materials based on colour.

Project Overview

This project combines computer vision, web technologies, and robotic control to create an automated waste-sorting system.

A camera is used to detect coloured cubes representing different types of waste. The computer-vision component processes the camera feed, identifies the colour of each cube, and classifies it into a waste category.

The detected object’s coordinates can then be passed to the robotic arm, allowing the system to select and pick up the appropriate cube.

System Architecture

Camera
   ↓
Computer Vision / AI Detection
   ↓
Colour & Object Classification
   ↓
Detection Coordinates
   ↓
Web Interface
   ↓
Robotic Arm
   ↓
Waste Sorting

🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* JavaScript
* React
* Raspberry Pi Pico
* Computer Vision
* REST API

AI Detection Component

File: src/model/cube_detector.py

The detection component uses OpenCV and HSV colour-space processing to identify coloured objects from a camera frame.

Main functionality

* Converts camera frames from BGR to HSV colour space.
* Uses HSV colour ranges to identify different coloured objects.
* Uses contour detection to locate objects in the camera feed.
* Filters out very small objects to reduce noise.
* Classifies detected objects according to their colour.
* Returns detection information that can be used by the robotic-control system.

Web Control Interface

File: web_interface/frontend/src/Control.js

The React frontend provides an interface for interacting with the robotic arm and AI detection system.

The control flow includes:

1. Requesting current detections from the AI backend.
2. Filtering detections by the requested colour.
3. Checking the confidence level of the detection.
4. Selecting the most confident detected cube.
5. Sending the cube’s coordinates to the robotic-arm backend.
6. Triggering the pickup operation.

Detection & Pickup Workflow

User selects cube colour
        ↓
Frontend requests AI detections
        ↓
AI identifies matching cubes
        ↓
Low-confidence detections are filtered
        ↓
Best detection is selected
        ↓
Coordinates are sent to robot
        ↓
Robotic arm performs pickup

Project Structure

Robotic-arm-sorting/
│
├── README.md
│
├── src/
│   └── model/
│       └── cube_detector.py
│
└── web_interface/
    └── frontend/
        └── src/
            └── Control.js

Project Objective

The goal of the project is to demonstrate how computer vision and robotics can be combined to automate material sorting.

The system was designed around the idea of reducing manual sorting by allowing a robotic arm to identify and interact with objects based on visual information.

Project Skills Demonstrated

* Computer vision
* Python programming
* Object detection
* Image processing
* REST API communication
* React frontend development
* Robotic-system integration
* Debugging and system integration
* Working with hardware and software together

Future Improvements

Possible improvements include:

* More robust object detection using a trained machine-learning model.
* Improved object-position calibration between the camera and robotic arm.
* Support for additional waste categories.
* Improved confidence scoring.
* A more advanced monitoring dashboard.
* Improved error handling between the frontend, detection service, and robotic controller.

Project Context

This project was developed as an academic robotics and software-development project and demonstrates the integration of multiple technologies into a single automated system.
