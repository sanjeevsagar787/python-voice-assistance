import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python
# Speech recognition allows the machine to turn the speech signal into text
import speech_recognition as sr
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib  # for sending mail
import wolframalpha  # To calculate strings into formulas



# he Speech Application Programming Interface or SAPI is an API developed
engine = pyttsx3.init('sapi5')
# by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanjeevsagarsagar3@gmail.com', 'password of mail')
    server.sendmail('sanjeevsagarsagar4@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Sagar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "who are you" in query or "define yourself" in query:
            speaks = '''Hello, I am Jarvis. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            speak(speaks)

        elif "who made you" in query or "created you" in query:
            speaks = "I have been created by Sanjeev Sagar."
            speak(speaks)

        elif "calculate" in query.lower():
            # write your wolframalpha app_id here
            app_id = "8AUXG2-VQ28659HXQ"
            client = wolframalpha.Client(app_id)

            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on Frank, I will show you where " + location + " is.")
            url='https://google.nl/map/place/' + location +'/&amp'
            webbrowser.get().open(url)
            print('Here is your location' + location)

        elif 'search' in query: 
            indx = query.lower().split().index('search') 
            query = query[1:] 
            url="https://www.google.com/search?q = " + "query"
            webbrowser.get().open(url)

        if "stop listening" in query:
            listening = False
            print('Listening stopped')

        elif 'email to sanjeev' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sanjeevsagarsagar4@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sanjeev. I am not able to send this email")
