"""
Please run this script outside the Docker container, as it requires access to the host's audio hardware.
"""

import serial
import struct
import time
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

# ----------------- Configuration -----------------
PORT = 'COM3'          # Change to your UART port
BAUDRATE = 921600      # Match your MCU UART baudrate
SYNC_WORD = 0xAA55     # Must match your MCU SYNC_WORD
RECORD_SECONDS = 5

# ----------------- Open serial -----------------
ser = serial.Serial(PORT, BAUDRATE, timeout=0.1)
print(f"Opened {PORT} at {BAUDRATE} baud")

start_time = time.time()
data_bytes = bytearray()

# ----------------- Record for 5 seconds -----------------
print(f"Recording {RECORD_SECONDS} seconds...")
while time.time() - start_time < RECORD_SECONDS:
    chunk = ser.read(1024)
    if chunk:
        data_bytes.extend(chunk)

ser.close()
print(f"Recording done, {len(data_bytes)} bytes received")

# ----------------- Extract samples -----------------
samples = []
i = 0
while i < len(data_bytes) - 2:
    # Check for sync word
    sync = struct.unpack_from('<H', data_bytes, i)[0]  # little-endian
    if sync == SYNC_WORD:
        i += 2
        # Extract following 16-bit samples until next sync word
        while i < len(data_bytes) - 1:
            next_sync = struct.unpack_from('<H', data_bytes, i)[0]
            if next_sync == SYNC_WORD:
                break
            sample = struct.unpack_from('<h', data_bytes, i)[0]  # signed 16-bit
            samples.append(sample)
            i += 2
    else:
        i += 1  # Move forward to find sync word

samples = np.array(samples, dtype=np.int16)
num_samples = len(samples)
actual_time = RECORD_SECONDS  # measured time
sample_rate = num_samples / actual_time

print("Playing back audio...")
sd.play(samples, samplerate=int(sample_rate))
sd.wait()  # Wait until playback finishes
print("Playback finished")

print(f"Received {num_samples} samples in {actual_time:.2f} seconds")
print(f"Approximate sample rate: {sample_rate:.2f} Hz")

# ----------------- Plot audio -----------------
plt.figure(figsize=(12,4))
plt.plot(samples, label='Audio samples')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.title('UART PCM Audio')
plt.grid(True)
plt.legend()
plt.show()
