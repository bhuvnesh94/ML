import speech_recognition as sr
import os
mic=sr.Microphone()
r=sr.Recognizer()
with mic as source:
    r.adjust_for_ambient_noise(source)
    print('say')
    audio=r.listen(source)
audio_input=r.recognize_google(audio)
print(audio_input)
if 'open chrome' in audio_input.lower():
    os.system("google-chrome")