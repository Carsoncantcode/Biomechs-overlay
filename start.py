import cv2
from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt')

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
out = None
recording = False
index=0

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = model.predict(im0,classes=0)
        
    annotated_frame = results[0].plot(labels=False, boxes=False, conf=1.0)

    cv2.imshow("Biomechs", annotated_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('r') and not recording:
        out = cv2.VideoWriter(f'output{index}.mp4', fourcc, fps, (w, h))
        recording = True
        print("recording started")
    elif key == ord('s') and recording:
        recording = False
        out.release()
        print("Recording stopped")
        index = index + 1
    
    if recording:
        out.write(annotated_frame)
    
    if key == ord('q'):
        break

if recording:
    out.release()
cap.release()     
cv2.destroyAllWindows()
