from pydub import AudioSegment
from pydub.playback import play
import time

def play_loud_beep(sound):
    sound = AudioSegment.from_file(sound, format="wav")  # Replace with the actual path to your audio file
    while True:
        play(sound)
        time.sleep(5)  # Wait for 5 seconds


sound = 'output.wav'  # Provide the correct path to your WAV audio file
play_loud_beep(sound)
