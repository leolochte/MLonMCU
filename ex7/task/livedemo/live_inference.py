import cv2
import serial
import threading
import numpy as np
import sys


CIFAR10_CLASSES = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]

def parse_input(input_string):
    parts = input_string.split()
    try:
        clk = int(parts[1])
        print(f"{parts[0]} is detected with {clk} clock cycles long inference ({clk / 80000000} s @ 80 MHz)")
    except:
        print("Catch")
        print(parts)


def preprocess_frame(frame):
    """
    1. Convert BGR to RGB
    2. Resize to 32x32
    3. Shift pixel values from [0, 255] to [-128, 127] (int8)
    4. Return flattened bytes
    """
    # Convert from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize to (32, 32)
    resized = cv2.resize(rgb_frame, (32, 32), interpolation=cv2.INTER_AREA)

    # Shift pixel values [0..255] -> [-128..127]
    resized_int32 = resized.astype(np.int32) - 128
    resized_int8 = resized_int32.astype(np.int8)

    # Flatten the image to a 1D array (32 * 32 * 3 = 3072 bytes)
    flattened = resized_int8.flatten()

    # Return as raw bytes
    return flattened.tobytes()

latest_frame = None
frame_lock = threading.Lock()


def camera_capture_thread(camera_index=0):
    """
    Continuously capture frames from the camera.
    """
    global latest_frame
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Error: Cannot open camera at index {camera_index}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            continue  # If frame isn't read correctly, skip

        with frame_lock:
            latest_frame = frame

        # Display the live feed
        cv2.imshow("Live Camera", frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def serial_read_thread(port='/dev/ttyACM0', baudrate=115200):

    global latest_frame

    ser = serial.Serial(port, baudrate, timeout=None)
    print("Serial port opened:", ser.name)

    while True:
        # Read line (blocking until \n)
        line = ser.readline().decode('utf-8').rstrip('\n')
        if "Waiting" in line:
            print("CIFAR10 Inference Demo is Started")
        elif (not "unknown" in line):
            parse_input(line)

        if line:
            # Microcontroller requests next image
            # Grab the most recent frame from the buffer
            with frame_lock:
                if latest_frame is not None:
                    # Preprocess frame
                    data = preprocess_frame(latest_frame)
                    
                else:
                    # If no frame yet, skip
                    continue

            # Send the preprocessed bytes
            ser.write(data)
            ser.flush()


def main(port='/dev/ttyACM0', baudrate=115200, camera_index=0):
    ser_thread = threading.Thread(target=serial_read_thread, 
                                  kwargs={'port': port, 'baudrate': baudrate},
                                  daemon=True)
    ser_thread.start()

    camera_capture_thread(camera_index=camera_index)

if __name__ == "__main__":
    # Use default values, or override them via command-line
    # Example usage: python3 camera_inference.py /dev/ttyACM0 115200

    port = "/dev/ttyACM0"
    baudrate = 115200

    if len(sys.argv) > 1:
        port = sys.argv[1]
    if len(sys.argv) > 2:
        baudrate = int(sys.argv[2])

    main(port=port, baudrate=baudrate)

