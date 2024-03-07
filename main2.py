import datetime
import shutil
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipediaapi
import openai


openai.api_key = 'api_key'

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good Morning Sir!")
    elif 12 <= hour < 18:
        say("Good Afternoon Sir!")
    else:
        say("Good Evening Sir!")

    assname = "deltaai 1.0"
    say(f"I am your Assistant {assname}")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def username():
    say("What should I call you sir?")
    uname = input("Please type Your name: ")
    say(f"Welcome Mister {uname}")
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))

    say("How can I help you, Sir")

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(query)
    return page_py.text[:500]  # Limiting the response to the first 500 characters

def search_openai(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Choose an appropriate model
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
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
    print("Hello, I am DELTA A.I.")
    wishMe()
    username()

    while True:
        print("Listening...")
        text = takecommand()
        

        if text.lower() == "exit".lower():
            print("Exiting...")
            say("Exiting...")
            break

        elif "open youtube".lower() in text:
            webbrowser.open("https://youtube.com")
            print("Opening Youtube Sir")
            say("Opening Youtube Sir")

        elif "open vit".lower() in text:
            webbrowser.open("https://vtop.vit.ac.in/vtop/login")
            print("Opening Vtop Sir")
            say("Opening Vtop Sir")

        elif "open flipkart".lower() in text:
            webbrowser.open("https://www.flipkart.com/")
            print("Opening Flipkart Sir")
            say("Opening Flipkart Sir")

        elif "flipkart".lower() in text:
            webbrowser.open("https://www.flipkart.com/")
            print("Opening Flipkart Sir")
            say("Opening Flipkart Sir")

        elif "search".lower() in text.lower():
            query = text.replace("search", "").strip()
            wiki_result = search_wikipedia(query)
            openai_result = search_openai(query)
            combined_result = f"Wikipedia says: {wiki_result}. OpenAI says: {openai_result}"
            print(combined_result)
            say(combined_result)

        elif text:
            response = search_openai(text)
            print(response)
            say(response)
            

