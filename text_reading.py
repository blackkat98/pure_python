import pyttsx3

ai = pyttsx3.init()

# voices = ai.getProperty('voices')
# girl_voice = voices.pop()
# ai.setProperty('voice', girl_voice.id)
# rate = ai.getProperty('rate')
# ai.setProperty('rate', rate - 8)

ai.say('résume')
# ai.save_to_file('hello world', 'audio/hello_world.mp3')
# ai.startLoop()
# ai.endLoop()
ai.runAndWait()