# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install requests
# pip install openai

from openai import OpenAI
import speech_recognition as sr
import webbrowser  # Built-in: to open URLs
import pyttsx3 as py  # For text-to-speech
import musiclib  # Custom module with predefined music URLs
import requests

newsapi = ""  # Your NewsAPI key
recognizer = sr.Recognizer()
engine = py.init()

# Function to speak given text using TTS engine
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Function to get OpenAI-generated response for a given prompt
def aiprocess(c):
    client = OpenAI(
        api_key="",  # Your API key for OpenAI (paid version)
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general task like Alexa and google cloud."},
            {"role": "user", "content": c}
        ]
    )
    return (completion.choices[0].message).content

# Function to handle user commands
def process(c):
    if (c.lower() == "open facebook"):
        webbrowser.open("https://facebook.com")
    elif (c.lower() == "open youtube"):
        webbrowser.open("https://youtube.com")
    elif (c.lower() == "open google"):
        webbrowser.open("https://google.com")
    elif (c.lower().startswith("play")):
        song = c.lower().split(" ")[1]  # Extracts the second word (song name)
        pick = musiclib.music[song]  # Get URL from musiclib dictionary
        webbrowser.open(pick)
    elif "news" in c.lower():
        s = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if s.status_code == 200:
            data = s.json()  # Parse JSON
            articles = data.get("articles", [])  # Extract article list
            print("Top US Headlines:\n")
            for article in articles:
                speak(article['title'])  # Speak each headline
        else:
            print(f"Error: Unable to fetch news (Status code: {s.status_code})")
    else:
        output = aiprocess(c)  # If no command matched, ask OpenAI
        speak(output)

# Main app entry point
if __name__ == "__main__":
    speak("Initializing the app")

# App listens for wake word "Jarvis"
while 1:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            recognizer.adjust_for_ambient_noise(source)
            word = recognizer.listen(source, phrase_time_limit=4)  # Short command listener

        command = recognizer.recognize_google(word)
        print(command)

        # Start full command mode if wake word is heard
        if (command.lower() == "jarvis"):
            while True:
                try:
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=3, phrase_time_limit=10)

                    command = recognizer.recognize_google(audio)
                    print("Command received:", command)
                    speak("You said " + command)
                    process(command)  # Handle command
                except Exception as e:
                    print("Error:", e)
                    speak("Sorry, there was an error.")
    except Exception as e:
        print(" error{0}".format(e))
