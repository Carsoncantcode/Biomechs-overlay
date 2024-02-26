# Import necessary libraries
import cv2
from ultralytics import YOLO

# Load the YOLO model from Ultralytics (yolov8n-pose.pt)
model = YOLO('yolov8n-pose.pt')

# Open a connection to the camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the frame width and height of the camera
cap.set(3, 1920)
cap.set(4, 1080)

# Check if the camera is opened successfully
assert cap.isOpened(), "Error reading video file"

# Get the frame width, height, and frames per second (fps) of the camera
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define the four-character code for the video codec (avc1 for H.264)
fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')

# Initialize the video writer and related variables
out = None
recording = False
index = 0

# Enter into a loop to capture and process video frames
while cap.isOpened():
    # Read a frame from the camera
    success, im0 = cap.read()

    # Check if the frame is successfully read
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    # Perform object detection using the YOLO model on the current frame
    results = model.predict(im0, classes=0)
        
    # Get the annotated frame with detected objects
    annotated_frame = results[0].plot(labels=False, boxes=False, conf=1.0)

    # Display the annotated frame in a window named "Biomechs"
    cv2.imshow("Biomechs", annotated_frame)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    
    # Start recording when 'r' key is pressed and not already recording
    if key == ord('r') and not recording:
        out = cv2.VideoWriter(f'output{index}.mp4', fourcc, fps, (w, h))
        recording = True
        print("Recording started")
    
    # Stop recording when 's' key is pressed and currently recording
    elif key == ord('s') and recording:
        recording = False
        out.release()
        print("Recording stopped")
        index += 1
    
    # Write annotated frames to the output video if recording
    if recording:
        out.write(annotated_frame)
    
    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release resources: video writer, camera, and close windows
if recording:
    out.release()
cap.release()     
cv2.destroyAllWindows()
