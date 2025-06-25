#Jarvis AI
import speech_recognition as sr
import win32com.client
import webbrowser
import wikipedia
import datetime
from config import apikey
import time
import os
import openai
import subprocess
import random



def ai(prompt):
    openai.api_key = apikey
    text=f"OpenAI response for Prompt: {prompt} \n**********"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write an email to my boss for resignation?",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    print(response["choices"][0]["text"])
    text+=response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open (f"Openai/prompt-{random.randint(1,23434356)}","w") as f:
        f.write(text)

speaker=win32com.client.Dispatch("SAPI.SpVoice")

if (time.strftime("%H"))>"0" and (time.strftime("%H"))<"12":
    print("Good morning Vijay")
    speaker.Speak(f"Good morning Vijay")
elif (time.strftime("%H"))>"12" and (time.strftime("%H"))<"18":
    print("Good Afternoon Vijay")
    speaker.Speak(f"Good Afternoon Vijay")
else :
    print("Good Evening Vijay")
    speaker.Speak(f"Good Evening Vijay")

print("My name is Jarvis")
speaker.Speak("My name is Jarvis ")

print("What can I do for you ?")
speaker.Speak("What can I do for you ?")

def say(text):
    speaker.Speak(f"{text}")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            print("Recognising...")
            query=r.recognize_google(audio,language="en-US")
            print(f"You Said : {query} ")
            return query
        except Exception as e:
            return "Some Error occured . Sorry from Jarvis"
    
    

if __name__=="__main__":
    print("Listeninnggg........")
    query=takecommand()
    sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.co.in"],["brave","https://search.brave.com/"],["googlemaps","https://www.google.com/maps/@18.5118933,73.9135265,15z?entry=ttu"],["instagram","https://www.instagram.com"],["facebook","https://www.facebook.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir.......")
            webbrowser.open(site[1])
        
    
    if "Jarvis the time is".lower() in query.lower():
        strftTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir the time is - {strftTime}")
        say(f"sir the time is{strftTime}")

    if "Jarvis who created you".lower() in query.lower():
        print(f"Master Vijay created me")
        say(f"Master Vijay created me")

    if "Jarvis when were you created".lower() in query.lower():
        print(f"I was created on 8 May 2024")
        say(f"I was created on 8 May 2024")

    if "Jarvis open camera".lower() in query.lower():
        print(f"Opening Camera")
        say(f"Opening Camera")
        os.system("start microsoft.windows.camera:")

    if "Jarvis open setting".lower() in query.lower():
        print("Opening settings")
        say("Opening settings")
        subprocess.Popen([r"C:\Windows\System32\DpiScaling.exe"])

    if "Jarvis open Notepad".lower() in query.lower():
        print("Opening Notepad")
        say("Opening Notepad")
        os.system('notepad.exe') 
        #starts notepad
    
    if 'Jarvis are you there'.lower() in query.lower():
        stMsgs = ['At you service, Sir']
        print('At you service, Sir')
        say(stMsgs)
    
    if 'What'.lower() in query.lower():
        print('Searching Wikipedia...')
        say('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia")
        say("According to Wikipedia")
        print(results)
        say(results)

    
    if 'Search in wikipedia'.lower() in query.lower():
        print('Searching Wikipedia...')
        say('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia")
        say("According to Wikipedia")
        print(results)
        say(results)

    if "Using artificial intelligence".lower() in query.lower():
        ai(prompt=query)
        
    if 'Jarvis shutdown the PC'.lower() in query.lower():
        choice = input("Please confirm to shutdown the pc (y or n)")
        say("Please confirm to shutdown the pc (y or n)")
        if choice == 'n':
            exit()
        else:
            say("shutting down p c")
            os.system("shutdown /s /t 1")

    if "Jarvis exit".lower() in query.lower():
        print("Ok sir, Take Care.")
        say("Ok sir, Take Care.")


    else:
            if 'Give me some information about '.lower() in query.lower():
                print('Searching Google...')
                say('Searching Google...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("According to Google")
                say("According to Google")
                print(results)
                say(results)

print("That's all for now! Remember, I'm here to help whenever you need.")
say("That's all for now! Remember, I'm here to help whenever you need.")
    

    