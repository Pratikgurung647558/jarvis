#pip install speechrecognition pyaudio
#pip install setuptools
#pip install pyttsx3

import speech_recognition as sr
import webbrowser  #builtin
import pyttsx3 as py  #for text to speech
import musiclib
engine=py.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    if(c.lower()=="open facebook"):
        webbrowser.open("https://facebook.com")
    elif(c.lower()=="open youtube"):
        webbrowser.open("https://youtube.com")
    elif(c.lower()=="open google"):
        webbrowser.open("https://google.com")
    elif(c.lower().startswith("play")):
        song=c.lower().split(" ")[1] #for taking the play din parts din as a input
        pick=musiclib.music[song]
        webbrowser.open(pick)

if __name__=="__main__":
    speak("Initializing the app")
#start when said jarvis

# obtain audio from the microphone
while 1:
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            recognizer.adjust_for_ambient_noise(source)
            word = recognizer.listen(source, phrase_time_limit=4 )   
        command=recognizer.recognize_google(word)
        print(command)
        #now after jarvis the command mode on
        if (command.lower()=="jarvis"):   
            while True:
                    try:
                        with sr.Microphone() as source:      
                            print("Listening for your command...")
                            recognizer.adjust_for_ambient_noise(source)
                            audio = recognizer.listen(source,timeout=3, phrase_time_limit=10)

                        command = recognizer.recognize_google(audio)
                        print("Command received:", command)
                        speak("You said " + command)
                        process(command)
                    except Exception as e:
                        print("Error:", e)
                        speak("Sorry, there was an error.")
    
    except Exception as e:
        print(" error{0}".format(e))