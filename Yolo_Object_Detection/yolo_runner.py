from ultralytics import YOLO
from ultralytics import YOLOWorld
import cv2
import time


# model = YOLO("../models/best.pt")
model = YOLOWorld("../models/yolov8x-worldv2.pt")

# Make this run for only 20 seconds
def runner(timer):
    start = time.time()
    while time.time()< start + timer:
        a=model.predict(source='0')
    cv2.destroyAllWindows()




runner(45)