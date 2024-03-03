import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import time
import pyautogui
import os
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import openai


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def calculate_math_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Sorry, I couldn't perform the calculation. Please try again."

openai.api_key = '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'



def open_spotify_and_play_music():
    subprocess.Popen(["spotify"])
    time.sleep(1) 
    pyautogui.press('space')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Hi Kunal! Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Hi Kunal! Good Afternoon!")   
    else:
        speak("Hi Kunal! Good Evening") 

    speak("I am Friday sir, please tell me how may I help you?")  

# def get_google_search_result(query):
#     try:
#         for j in search(query, num=1, stop=1, pause=2):
#             response = requests.get(j)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             result_text = ""
#             paragraphs = soup.find_all('p')
#             for paragraph in paragraphs[:3]:
#                 result_text += paragraph.text
#             return result_text
#     except requests.exceptions.ConnectionError:
#         return "Sorry, I couldn't retrieve the search results due to a connection issue. Please check your internet connection and try again later."


def takeCommand():
    # it takes microphone input from user and returns string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again, please!")
        return "None"
    return query

    

if __name__=="__main__":
    wishMe()
    while 1:
        query=takeCommand().lower()
        if 'quit' in query  or 'stop' in query:
            speak("ok sir!")
            break
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open('youtube.com')   
        
        elif 'open chat gpt' in query:
            speak("Opening chat gpt")
            webbrowser.open('https://chat.openai.com/')

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open('google.com')    

        elif 'open whatsapp' in query:
            speak("Opening whatsapp web")
            webbrowser.open('web.whatsapp.com')
        
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H o'clock %M minutes %S seconds ")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open' in query and 'code' in query:
            codePath="C:\\Users\kunal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio code")
            os.startfile(codePath)
        
        elif 'open word' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening Microsoft word")
            os.startfile(codePath)
        
        elif 'open excel' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            speak("Opening Microsoft excel")
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            speak("Opening Microsoft Powerpoint")
            os.startfile(codePath)  

        elif 'open chrome' in query:
            codePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening Chrome Browser")
            os.startfile(codePath)       
                    
        elif 'play spotify' in query or 'play song' in query or 'open spotify' in query:
            speak("opening spotify")
            open_spotify_and_play_music()
        
        elif 'youtube' in query:
            speak("Searching on youtube")
            query=query.replace("search","")
            query = query.replace("youtube", "")
            webbrowser.open(f"https://www.youtube.com/search?q={query}")
             
        elif 'google' in query or 'search' in query or 'image' in query or 'images' in query or 'video' in query or 'videos' in query:
            speak("Searching on Google")
            query = query.replace("google", "")                                                              
            query=query.replace("search","")
            webbrowser.open(f"https://www.google.com/search?q={query}")
          
         
        elif 'who are you' in query or 'your name' in query or 'yourself' in query:
            print("I am Friday sir, Female Replacement Intelligent Digital Assitant Youth")
            speak("I am Friday sir, Female Replacement Intelligent Digital Assitant Youth")
        
        elif 'close' in query:
            speak("closing the window")
            pyautogui.keyDown('win')
            pyautogui.press('d')
            pyautogui.keyUp('win')


        # else:
        #     google_result = get_google_search_result(query)
        #     print(google_result)
        #     speak("Here are the search results:")
        #     speak(google_result)      
            
        # else:
        #     speak("Let me search that for you")
        #     # query=query.replace("wikipedia","")
        #     results=wikipedia.summary(query,sentences=6)
        #     print(results)
        #     speak(results)
        
        else:
            query=query.replace("Friday","")
            completion= openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":f"{query}"}])
            print(completion.choices[0].message.content)
            speak(completion.choices[0].message.content)