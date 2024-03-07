import datetime
import shutil
import pyttsx3
import speech_recognition as sr
import webbrowser

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good Morning Sir!")
    elif 12 <= hour < 18:
        say("Good Afternoon Sir!")
    else:
        say("Good Evening Sir!")
        
    print("Hello, I am DELTA A.I.")
    assname = "Hello, I am DELTA A.I."
    say(f"I am your Assistant {assname}")
    
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def username():
    say("What should I call you sir?")
    uname = input("Your name: ")
    say(f"Welcome Mister {uname}")
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))

    say("How can I help you, Sir")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you please repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

if __name__ == '__main__':
    wishMe()
    username()
    
    while True:
        print("Listening...")
        text = takecommand()
        
        if text == "exit":
            print("Exiting...")
            break
        
        if "open youtube".lower() in text.lower():
            webbrowser.open("https://youtube.com")
            print("Opening Youtube Sir")
            say("Opening Youtube Sir")
            
        elif "open vit".lower() in text.lower():
            webbrowser.open("https://vtop.vit.ac.in/vtop/login")
            print("Opening Vtop Sir")
            say("Opening Vtop Sir")
            
        elif "open flipkart".lower() in text.lower():
            webbrowser.open("https://www.flipkart.com/")
            print("Opening Flipkart Sir")
            say("Opening Flipkart Sir")
            
        elif "Flipkart".lower() in text.lower():
            webbrowser.open("https://www.flipkart.com/")
            print("Opening Flipkart Sir")
            say("Opening Flipkart Sir")
            
            
        elif text:
            say(text)
