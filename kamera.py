import pyzed.sl as sl
import cv2

def main():
    # Create a ZED camera object
    zed = sl.Camera()
    # Create a ZED camera object
    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080
    init_params.camera_fps = 30

    # Open the ZED camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Kamera calismiyor {str(err)}")


    # Set up the camera runtime parameters
    runtime_params = sl.RuntimeParameters()

    while True:
        # Capture a frame from the camera
        if zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            # Retrieve the left image
            image = sl.Mat()
            zed.retrieve_image(image, sl.VIEW.VIEW_LEFT)

            # Convert the image to a format suitable for OpenCV
            frame = image.get_data()

            # Display the frame using OpenCV
            cv2.imshow("ZED Camera", frame)

            # Exit the loop when the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Close the camera
    zed.close()

main()