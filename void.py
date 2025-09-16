import os
import pyttsx3
from datetime import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
from youtubesearchpython import VideosSearch
import pyjokes
import pyautogui
import google.generativeai as genAI
from dotenv import load_dotenv
import random
import platform
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

load_dotenv()
api_key = os.getenv("API_KEY")
genAI.configure(api_key=api_key)
model = genAI.GenerativeModel("gemini-2.0-flash")

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
    
def wishme():
    hour_now = int(datetime.now().hour)
    if hour_now>0 and hour_now<12:
        greeting = "Ah, morning. Everyone's favorite nightmare."
    elif hour_now>12 and hour_now<15:
        greeting = "Afternoon already? Time well wasted."
    else:
        greeting = "Evening. Because what could possibly go wrong now?"
        
    print(greeting)
    speak(greeting)
    
listening_lines = [
    "let's hear whatever this is...",
    "umm...",
    "this better involve actual words...",
    "speak, maybe...",
    "speak in english...",
    "let's go...",
    "let's suffer...",
    "do it..."
]

failed_listening_lines = [
    "that was not english.",
    "you call that speaking?",
    "zero clue of what you just said!",
    "you didn't say it or my ears just broke.",
    "volume up, babygurll.",
    "speak louder, i ain't a mind reader....yet!",
    "did you fail your english class?",
    "something stuck in your mouth?"
]

timeout_lines = [
    "I'll just wait over.",
    "you done? or never started.",
    "you said nothing, and i noticed.",
    "aren't you dead yet.",
    "you ghosted me live.",
    "the silence is louder than you."
]

def take_instructions():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        line = random.choice(listening_lines)
        print(line)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        try_lines = random.choice(timeout_lines)
        print(try_lines)
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        failed_lines = random.choice(failed_listening_lines)
        print(failed_lines)
        return "none"

    return query

def take_screenshot():
    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{time_now}-screenshot.jpg"
    image = pyautogui.screenshot(file_name)
    print(f"Took a screenshot and saved as {file_name}")
    speak("Took a screenshot!")

def searchyoutube(query):
    search = VideosSearch(query, limit=1)
    result = search.result()['result'][0]
    video_url = result['link']
    webbrowser.open(video_url)

def is_windows():
    try:
        system = platform.system()
        return system == "Windows"
        
    except Exception as e:
        print(f"Some error occured while testing the OS: {e}")
        return False

def start_app(app_name):
    prompt = model.generate_content(f"Extract the exact app name from this user command for opening applications Only provide the app name as a single word or standard command. Do not add extra text, explanations, or punctuation: '{app_name}'")
    
    app_name = prompt.text.strip()
    
    try:
        subprocess.run([app_name], shell=True)
        print(f"SApp Started: {app_name}")
        
    except FileNotFoundError:
        print(f"\n{app_name} not found! Make sure it's installed and in PATH.")
        
    except Exception as e:
        print(f"Some Unknown Error Occured: {e}")
        
def print_speak(query):
    print(query)
    speak(query)

if __name__ == "__main__":
    wishme()
    while True:
        query = take_instructions().lower()
        if 'wikipedia' in query:
            speak("Let me search the Wikipedia...")
            query = query.replace("wikipedia", "")
            searchResults = wikipedia.summary(query, sentences=2)
            print(f"As per the wikipedia,  {searchResults}")
            speak("As per the Wikipedia, ")
            speak(searchResults)

        elif "open" in query:
            if "youtube" in query:
                url, name = "https://youtube.com", "YouTube"
            elif "google" in query:
                url, name = "https://google.com", "Google"
            elif "linkedin" in query:
                url, name = "https://linkedin.com", "LinkedIn"
            elif "github" in query:
                url, name = "https://github.com", "GitHub"
            elif "stack overflow" in query:
                url, name = "https://stackoverflow.com", "Stack Overflow"
            elif "instagram" in query:
                url, name = "https://instagram.com", "Instagram"
            elif "whatsapp" in query:
                url, name = "https://web.whatsapp.com", "WhatsApp"
            elif "amazon" in query:
                url, name = "https://amazon.in", "Amazon"
            elif "geekforgeeks" in query:
                url, name = "https://geeksforgeeks.org", "GeeksForGeeks"
            elif "w3 schools" in query:
                url, name = "https://w3schools.com", "W3Schools"
            elif "twitter" in query or "x" in query:
                url, name = "https://x.com", "X"
            elif "chatgpt" in query:
                url, name = "https://chat.openai.com", "ChatGPT"
            elif "reddit" in query:
                url, name = "https://reddit.com", "Reddit"
            elif "microsoft" in query:
                url, name = "https://microsoft.com", "Microsoft"
            elif "pinterest" in query:
                url, name = "https://pinterest.com", "Pinterest"
            elif "duck duck go" in query:
                url, name = "https://duckduckgo.com", "Duck Duck Go"
            elif "weather" in query:
                url, name = "https://weather.com", "Weather"
            elif "quora" in query:
                url, name = "https://quora.com", "Quora"
            elif "telegram" in query:
                url, name = "https://web.telegram.org", "Telegram"
            elif "zoom" in query:
                url, name = "https://zoom.us", "Zoom"
            else:
                speak("Sorry, I don't recognize that site.")
                continue

        elif "stop" in query:
            print("\nBye! Catch You Later.")
            speak("Bye! Catch You Later.")
            break

        elif "the time" in query:
            theTime = datetime.datetime.now().strftime("%H : %M : %S")
            print(theTime)
            time = "It is" + theTime
            speak(time)

        elif "open" in query and "code" in query:
            start_app(query)
            print_speak("Opening VS Code!")
            break

        elif "open" in query and "photoshop" in query:
            start_app(query)
            print_speak("Opening Photoshop!")
            break

        elif "open" in query and "notepad" in query:
            start_app(query)
            print_speak("Opening Notepad!")
            break

        elif "open" in query and "filmora" in query:
            start_app(query)
            print_speak("Opening Filmora!")
            break

        elif "open" in query and "after effects" in query:
            start_app(query)
            print_speak("Opening Filmora!")
            break

        elif "open" in query and "vlc" in query:
            start_app(query)
            print_speak("Opening VLC!")
            break

        elif "open" in query and "chrome" in query:
            start_app(query)
            print_speak("Opening Google Chrome!")
            break
            break

        elif "open" in query and "media encoder" in query:
            start_app(query)
            print_speak("Opening Adobe Media Encoder!")
            break

        elif "open" in query and "audacity" in query:
            start_app(query)
            print_speak("Opening Audacity!")
            break

        elif "open" in query and "github desktop" in query:
            start_app(query)
            print_speak("Opening GitHub!")
            break

        elif "open" in query and "7 zip" in query:
            start_app(query)
            print_speak("Opening 7-Zip!")
            break

        elif "open" in query and "excel" in query:
            start_app(query)
            print_speak("Opening MS Excel!")
            break

        elif "open" in query and "word" in query:
            start_app(query)
            print_speak("Opening MS Word!")
            break

        elif "open" in query and "powerpoint" in query:
            start_app(query)
            print_speak("Opening MS Powerpoint!")
            break

        elif "open" in query and "explorer" in query:
            if(is_windows()):
                start_app(query)
                print_speak("Opening Explorer!")
                break
            else:
                print("This module doesn't support OS other than Windows!")

        elif "open" in query and "paint" in query:
            start_app(query)
            print_speak("Opening Paint!")
            break

        elif "play" in query and "on youtube" in query:
            query = query.replace("on youtube", "")
            query = query.replace("play", "").capitalize()
            print(f"Looking for {query}!")
            searchyoutube(query)
            query = f"Looking for {query}!"
            speak(query)
            break

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "text" in query:
            if(is_windows()):
                query = query.replace("text", "")
                print(f"Writing: {query}")
                pyautogui.typewrite(query)
            else:
                print("This module doesn't support OS other than Windows!")

        elif "explain" in query:
            query = query.replace("explain", "")
            response = model.generate_content(query)
            print(response.text)
            speak(response.text)

        elif "take a screenshot" in query:
            if(is_windows()):
                take_screenshot()
            else:
                print("This module doesn't support OS other than Windows!")

        else:
            response = model.generate_content(query)
            print(response.text)
            speak(response.text) 