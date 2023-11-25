import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

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
transform_audio_into_text()













