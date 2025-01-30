import cv2
import numpy as np
import pyautogui


def screen_record():
    resolution = (1920, 1080)
    fps = 60.0
    output_file_name = "output.avi"
    codec = cv2.VideoWriter.fourcc(*"XVID")
    output_file = cv2.VideoWriter(output_file_name, codec, fps, resolution)

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 360)

    while True:
        images = pyautogui.screenshot()
        frames = np.array(images)
        recording = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
        output_file.write(recording)

        cv2.imshow("Live", recording)

        if cv2.waitKey(1) == ord('q'):
            break

    output_file.release()
    cv2.destroyAllWindows()
    return output_file_name


test = screen_record()
print(test)
