from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics
import os


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
#output_dir = "Recoded_videos"
#os.makedirs(output_dir, exist_ok=True)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = ( f'{time_stamp}.mp4')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))


print(width, height)


# Uncomment if you want to include the webcam in the recording
# webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 10, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # Uncomment and adjust if you want to include the webcam in the recording
    # _, frame = webcam.read()
    # fr_height, fr_width, _ = frame.shape
    # img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]

    cv2.imshow('screen recorder', img_final)

    # Uncomment if you want to show the webcam feed separately
    # cv2.imshow('webcam', frame)

    if cv2.waitKey(10) == ord('q'):
        break

if __name__ == "__main__":

    cv2.destroyAllWindows()
    captured_video.release()




# Uncomment if using the webcam
# webcam.release()
