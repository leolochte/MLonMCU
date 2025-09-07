"""
Please run this script outside the Docker container, as it requires access to the host's audio hardware.
"""

import sounddevice as sd
import numpy as np
import wave

# ================== CONFIG ==================
DURATION = 5       # seconds to record
SAMPLE_RATE = 44100  # Hz
CHANNELS = 1       # Mono
OUTPUT_FILE = 'recording.wav'
# ============================================

def main():
    print(f"Press ENTER to start recording {DURATION} seconds of audio...")
    _ = input()
    print("Recording...")

    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32')
    sd.wait()  # Wait until recording is finished

    print("Recording finished. Playing back...")
    sd.play(recording, samplerate=SAMPLE_RATE)
    sd.wait()

    # Save to WAV
    print(f"Saving recording to {OUTPUT_FILE}...")
    recording_int16 = np.int16(recording * 32767)  # Convert to int16
    with wave.open(OUTPUT_FILE, 'w') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(recording_int16.tobytes())

    print("Playback and save finished.")

if __name__ == "__main__":
    main()
