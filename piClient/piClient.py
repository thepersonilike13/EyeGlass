import requests
import base64
from PIL import Image
from io import BytesIO
from yolo_runner import runner
from tts import speak
import argparse
import time
from transcription import main_stt
# Text to be converted to speech

def obj():
    raspberry_pi_ip = '192.168.137.35'  # Replace with your Raspberry Pi's IP address

    # Capture image from Raspberry Pi
    response = requests.get(f'http://{raspberry_pi_ip}:80/capture_image')
    image_data_base64 = response.json()['image']

    # Decode base64 data
    image_data = base64.b64decode(image_data_base64)

    # Save decoded image to file
    with open('captured_image.jpg', 'wb') as f:
        f.write(image_data)

    # Open and display the image
    image = Image.open(BytesIO(image_data))

    objects=runner(image)
    print(objects)
    detected_objects = {
        'objects': objects[0]
    }
    t=f"There is a {str(objects[0])} in front of you. Please be careful."
    speak(t)
# response=response = requests.post(f'http://{raspberry_pi_ip}:80/receive_detected_objects', json=detected_objects)
# image.show()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pi Client')
    parser.add_argument('--mode', type=str, default='OBJ', help='Enter OBJ for object detection mode \n SIGN for sign language mode \n SPEECH for speech transciption mode ')
    return parser.parse_args()



if __name__ == '__main__':
    args = parse_arguments()
    if args == 'OBJ':
        while True:
            obj()
            time.sleep(5)
    elif args == 'SPEECH':
        main_stt()
        

    # Rest of the code...