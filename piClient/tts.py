from gtts import gTTS
from playsound import playsound

import os
def speak(text):
  """Converts text to speech and plays the audio."""
  tts = gTTS(text=text, lang='en')  # Change 'en' for other languages
  tts.save("temp.mp3")  # Saves the audio to a temporary file
  playsound("temp.mp3")  # Plays the temporary audio file
  
  # Clean up the temporary file
  os.remove("temp.mp3")

# Example usage

