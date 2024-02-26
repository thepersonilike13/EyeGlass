from ultralytics import YOLO
import cv2
import time


model = YOLO('yolov8m.pt')

# Make this run for only 20 seconds
def runner(timer):
    start = time.time()
    while time.time()< start + timer:
        results = model.predict(source='0',show=True)
    cv2.destroyAllWindows()


runner(10)