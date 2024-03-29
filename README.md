# Sensory-Enhanced Eyeglasses Project

## Overview

The Sensory-Enhanced Eyeglasses Project is aimed at developing specialized eyewear for individuals who face challenges in speaking, hearing, or seeing. By integrating innovative technology and thoughtful design, our project seeks to enhance the sensory experience and interaction with the surrounding environment for these individuals.

## Object Detection Module

This module focuses on implementing object detection functionality within the sensory-enhanced eyeglasses. Through the use of state-of-the-art object detection algorithms, the eyeglasses can recognize and interpret objects in the user's vicinity, providing valuable contextual information.

### Requirements

- Python 3.x
- Ultralytics YOLO library
- OpenCV

### Usage

To run the object detection module, follow these steps:

1. Clone or download the repository containing the project files:
  ```
  git clone https://github.com/thepersonilike13/EyeGlass.git
  ```

2. Install the required dependencies if not already installed:
    ```
    pip install -r requirements.txt
    ```

3. Navigate to the directory containing the project files.

4. Execute the `app.py` script to initiate the object detection process:
    ```
    python app.py
    ```

5. The object detection module will run for a specified duration (default: 20 seconds) and display the results in a window. Detected objects will be highlighted in the displayed frames.

6. Once the specified duration elapses, the program will automatically close, and the results will be accessible through the terminal.



