# Screen Recorder in Python

This is a simple screen recorder built using Python. It captures the screen and saves it as a video file using `pyautogui`, `numpy`, and `cv2` (OpenCV).

## Features
- Records the entire screen
- Saves output as an AVI video file
- Uses OpenCV for video encoding
- Lightweight and easy to use

## Requirements
Make sure you have **Python 3.6+** installed on your system.

## Installation
To install the required dependencies, run:

```sh
pip install pyautogui numpy opencv-python
```

## How It Works
The screen recorder works as follows:
1. **Capture Screen**: Uses `pyautogui.screenshot()` to capture the screen frame by frame.
2. **Convert to NumPy Array**: Converts the screenshot to a NumPy array.
3. **Convert RGB to BGR**: OpenCV uses BGR format, so the frame is converted accordingly.
4. **Write to Video File**: Uses `cv2.VideoWriter` to save the frames as a video.
5. **Stop Recording**: Press `'q'` to stop the recording and save the file.

## Usage
Run the script using:

```sh
python screen_recorder.py
```

## Example Code
Here is a basic implementation of the screen recorder:

```python
import cv2
import numpy as np
import pyautogui

# Define screen resolution
screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 20.0, screen_size)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
```

## Stopping the Recorder
Press `'q'` to stop the recording and save the video file.

## Output File
The recorded video will be saved as:
```sh
screen_record.avi
```

## Troubleshooting
- If you encounter a `pyscreeze` error, try reinstalling dependencies:
  ```sh
  pip install --upgrade pyautogui pyscreeze pillow
  ```
- Ensure your Python version is **3.6+** for compatibility.

## License
This project is open-source and free to use.

---

Enjoy recording your screen! 🚀
## Thank You
[Author](https://github.com/abhinandan2540)

