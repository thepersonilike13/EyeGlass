import cv2
import time





def cam_segment(timer):
    start = time.time()
    while time.time() < start + timer:

        # Capture the video from the webcam in RGB
        cap = cv2.VideoCapture(0)

        # set width and height splitting the camera input into 3 frames
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Setting boundaries
        left_boundary = int(width / 3)
        right_boundary = int(2 * width / 3)
        ret, frame = cap.read()
        if not ret:
            break

        # Splitting the frame into 3 parts
        left_area = frame[:, :left_boundary, :]
        center_area = frame[:, left_boundary:right_boundary, :]
        right_area = frame[:, right_boundary:, :]

        # Displaying the split areas
        # cv2.imshow('Left Area', left_area)
        cv2.imshow('Center Area', center_area)
        # cv2.imshow('Right Area', right_area)
        # Show the entire frame
        # cv2.imshow('Entire Frame', frame)

        # Release the capture
    cap.release()
    cv2.destroyAllWindows()


cam_segment(45)




# from ultralytics import YOLO
# from ultralytics import YOLOWorld
# import cv2
# import time
# import numpy as np


# # model = YOLO("../models/best.pt")
# model = YOLOWorld("../models/yolov8x-worldv2.pt")

# # Make this run for only 20 seconds
# def runner(timer):
#     start = time.time()
#     while time.time()< start + timer:
#         predictions = model.predict(source='0',show=True,stream=True)
#         print(predictions)
#         print(type(predictions))
#     cv2.destroyAllWindows()




# # Make this run for only 20 seconds
# def runner(timer):
#     start = time.time()
#     while time.time() < start + timer:
#         # Capture frame from video source (replace '0' with your video path if needed)
#         frame = cv2.VideoCapture(0).read()[1]

#         # Perform prediction
#         results = model.predict(frame)
#         mask = np.zeros_like(frame, dtype=np.uint8)
#         # Process results to extract class names for persons
#         if results:  # Check if any objects were detected
#             for result in results:
#                 # Iterate through each detected object
#                 for box in result.boxes:
#                     class_id = int(box.cls.item())  # Get class index
#                     class_name = model.names[class_id]  # Get class name from model.names

#                     # Check if class name is "person" (adjust based on your model's class names)
#                     if class_name == "person":
#                         x_min, y_min, x_max, y_max = list(map(int,box.xyxy[0]))  # Extract bounding box coordinates
#                         cv2.rectangle(mask, (x_min, y_min), (x_max, y_max), (255, 255, 255), -1)  # Fill person area with white in mask

#                         # Optionally display class name (adjust font and color as needed)
#                         cv2.putText(frame, class_name, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

#         # Invert mask (optional, comment out if you want white person regions on black background)
#         mask = 255 - mask

#         # Apply mask
#         masked_frame = cv2.bitwise_and(frame, mask)

#         # Display the frame with detections
#         cv2.imshow("Person Detection", frame)
#         if cv2.waitKey(1) == ord("q"):  # Exit on 'q' press
#             break

#     cv2.destroyAllWindows()


# runner(20)
