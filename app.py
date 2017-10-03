import os
import time
import json
from gtts import gTTS
from pygame import mixer
from tinytag import TinyTag
from difflib import get_close_matches

mixer.init()
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[word]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't undestand your entry"
    else:
        return "The word doesn't exist. Please double check it."

def speak(item):
    tts = gTTS(text=item, lang='en')
    tts.save("good.mp3")
    tag = TinyTag.get('good.mp3')
    mixer.music.load("good.mp3")
    mixer.music.play()
    time.sleep(tag.duration)

word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item, 'listening...')
        speak(item)
else:
    print(output, 'listening...')
    speak(output)

