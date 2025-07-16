#pip install speechrecognition pyaudio
#pip install setuptools
#pip install puttsx3

import speech_recognition as sr
import webbrowser  #builtin
import pyttsx3 as py  #for text to speech

reconizer=sr.Recognizer()
engine=py.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing the app")

#start when said jarvis

# obtain audio from the microphone
while 1:
    

    # recognize speech using google
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source,timeout=5, phrase_time_limit=10)   #listen for only 2 sec
        command=recognizer.recognize_google(audio)
        print(command)
    
    except Exception as e:
        print(" error{0}".format(e))


 
