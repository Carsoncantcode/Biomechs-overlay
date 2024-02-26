# Import the OpenCV library
import cv2

# Define a function to list available cameras
def listCameras(max_to_test=10):
    # Initialize an empty list to store available camera indices
    availableCameras = []

    # Iterate through camera indices up to the specified maximum
    for i in range(max_to_test):
        # Create a VideoCapture object for the current camera index using CAP_DSHOW backend
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

        # Check if the VideoCapture object is successfully opened
        if cap.isOpened():
            # If opened, the camera is available, so add its index to the list
            availableCameras.append(i)

            # Release the VideoCapture object to free up resources
            cap.release()

    # Return the list of available camera indices
    return availableCameras

# Call the listCameras function and store the result in availableCameras variable
availableCameras = listCameras()

# Print the list of available cameras
print("Available Cameras:", availableCameras)
