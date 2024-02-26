import cv2

def listCameras(max_to_test=10):
    availableCameras = []
    for i in range(max_to_test):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            availableCameras.append(i)
            cap.release()
    return availableCameras
availableCameras = listCameras()
print("Available Cameras:", availableCameras)