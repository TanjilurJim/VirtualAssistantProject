import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Voice/Language options
id1 ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


#hear the microphone and return the audio as text
def transform_audio_into_text():
    # store recognizer in variable
    r = sr.Recognizer()

    #set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8
        # report that recording has begun
        print("you can now speak: ")
        #save what u hear as audio
        audio = r.listen(source)

        try:
            #search on google
            request = r.recognize_google(audio, language="en-us")

            #test in text
            print("You said " + request)

            #return request
            return request
        #in case it doesn't understand
        except sr.UnknownValueError:
            #show proof that it didn't understand the audio
            print("Oops! I didn't understand audio")

            #return error
            return "I am still listening"

        #in Case the request cannot be resolved
        except sr.RequestError:
            # show proof that it didn't understand the audio
            print("Oops! I didn't understand audio")

            # return error
            return "I am still listening"

        #Unexpected error
        except:
            # show proof that it didn't understand the audio
            print("Oops! something went wrong")

            # return error
            return "I am still listening"
# transform_audio_into_text()

#function so the assistant can be heard
def speak(message):

    #start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id2)

    #deliver message
    engine.say(message)
    engine.runAndWait()

    # Provide feedback to the user
    print(f"Assistant: {message}")



# speak("Hello World")

engine = pyttsx3.init()

# for voice in engine.getProperty('voices'):
#     print(voice)

#Inform day of the week
def ask_day():
    #create a variable with today's information
    day = datetime.date.today()
    print(day)

    #create day of the week

    week_day = day.weekday()
    print(week_day)

    #Names of days
    calendar = {0:"Monday",
                1:"Tuesday",
                2:"wednesday",
                3:"thursday",
                4:"friday",
                5:"Saturday",
                6:"Sunday"}
    #say the day
    speak(f'Today is, {calendar[week_day]}')

# ask_day()

def initial_greeting():

    # Say greeting
    speak('Hello I am Hazel. How can I help you?')


# Main function of the assistant
def ask_time():
    pass


def my_assistant():

    # Activate the initial greeting
    initial_greeting()

    # Cut-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            print("Opening YouTube...")
            continue
        elif 'open browser' in my_request:
            speak ('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            print("Opening the browser...")
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what time it is' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak('I am looking for it')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=1)
            speak('according to wikipedia: ')
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak('of course, right now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('this is what i found')
            continue
        elif 'play' in my_request:
            speak('oh, what a great idea! I´ll play it right now')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                speak('I am sorry, but I did not find it')
                continue
        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break


my_assistant()



# speak("Hello Jim. I hope you have a nice day")










