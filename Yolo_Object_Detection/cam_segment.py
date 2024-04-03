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
        # cv2.imshow('Center Area', center_area)
        # cv2.imshow('Right Area', right_area)
        # Show the entire frame
        cv2.imshow('Entire Frame', frame)

        # Release the capture
    cap.release()
    cv2.destroyAllWindows()


cam_segment(45)
