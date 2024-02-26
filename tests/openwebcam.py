# Import the OpenCV library
import cv2

# Create a VideoCapture object to capture video from the camera (camera index 1)
source = cv2.VideoCapture(1)

# Define the window name
win_name = 'camera'

# Create a named window with normal size
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Enter into a loop until the user presses the 'Esc' key (ASCII code 27)
while cv2.waitKey(1) != 27:
    # Read a frame from the video source
    has_frame, frame = source.read()

    # Check if the frame is successfully read
    if not has_frame:
        # Break the loop if there is no frame
        break

    # Display the current frame in the created window
    cv2.imshow(win_name, frame)

# Release the video source (release the camera)
source.release()

# Destroy the created window
cv2.destroyWindow(win_name)
