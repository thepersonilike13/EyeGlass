from ultralytics import YOLO
from ultralytics import YOLOWorld
import cv2
import time

def photo():
    cap = cv2.VideoCapture(0)  # 0 represents the default camera index

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open the camera")
    else:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Failed to capture frame from the camera")
        else:
            # Display the captured frame
            cv2.imshow('Camera', frame)
            cv2.waitKey(0)  # Wait for any key press to close the window
            return frame
            cap.release()

# Release the VideoCapture object and close the window

# model = YOLO("../models/best.pt")
model = YOLO("../models/yolov8x-worldv2.pt")

# Make this run for only 20 seconds
def runner(photo):
    start = time.time()
    name = []
    results = model.predict(photo,stream=True)
    # print(*results)
    for result in results:

        detection_count = result.boxes.shape[0]

        for i in range(detection_count):
            cls = int(result.boxes.cls[i].item())
            name.append(result.names[cls])
            confidence = float(result.boxes.conf[i].item())


            print(name)
    return name

    cv2.destroyAllWindows()



