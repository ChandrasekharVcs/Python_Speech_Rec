from gtts import gTTS
from playsound import playsound
f = open("speech.txt", 'r')
data = f.read()
print(data)
f.close()
