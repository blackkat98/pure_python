import speech_recognition
import pyttsx3

ai_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    audio = ai_ear.listen(mic)

try:
    text = ai_ear.recognize_google(audio)
except:
    text = 'I cannot recognize'

ai_mouth = pyttsx3.init()
voices = ai_mouth.getProperty('voices')
girl_voice = voices.pop()
ai_mouth.setProperty('voice', girl_voice.id)
ai_mouth.say(text)
ai_mouth.runAndWait()

