import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import smtplib
import requests
from bs4 import BeautifulSoup


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

# Global variable to keep track of the conversation context
# expecting_yes_no = False

# def respond_to_okay():
#     global expecting_yes_no
#     response_message = "Everything is set. Do you need anything else?"
#     speak(response_message)
#     print(f"Assistant: {response_message}")
#     expecting_yes_no = True  # Now expecting a yes/no response
#
# def handle_yes_no_response(response):
#     global expecting_yes_no
#     if response == "yes":
#         speak("How can I assist you further?")
#     elif response == "no":
#         speak("Okay, let me know if you need anything later.")
#     expecting_yes_no = False  # Reset the flag after handling


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


# Define a dictionary to store contact information (name to phone number mapping)
contact_info = {
    'Gym': '01791557014',
    'Alice': '+9876543210',
    # Add more contacts as needed
}

# Function to lookup a phone number based on a contact's name
def lookup_phone_number(contact_name):
    return contact_info.get(contact_name, None)



# speak("Hello World")

engine = pyttsx3.init()

# for voice in engine.getProperty('voices'):
#     print(voice)

#Inform day of the week
def ask_day():
    # Fetch the current date
    today = datetime.date.today()
    # Get the name of the day
    week_day = today.strftime("%A")
    # Format the date
    date_string = today.strftime("%B %d, %Y")  # Example: December 05, 2023
    # Announce the day and date
    speak(f"Today is {week_day}, {date_string}")


# ask_day()

def initial_greeting():

    # Say greeting
    speak('Hello I am Hazel. How can I help you?')


# Main function of the assistant
def ask_time():
    # Fetch the current time
    now = datetime.datetime.now()
    # Format the time as hour and minutes
    time_string = now.strftime("%H:%M")
    # Announce the time
    speak(f"The time is {time_string}")
def ask_date_and_time():
    # Fetch the current date and time
    now = datetime.datetime.now()
    # Get the name of the day and the formatted date and time
    week_day = now.strftime("%A")
    date_string = now.strftime("%B %d, %Y")
    time_string = now.strftime("%H:%M")
    # Announce the day, date, and time
    speak(f"Today is {week_day}, {date_string}. The time is {time_string}")

# Function for web scraping
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract information from the website using BeautifulSoup
        # You can print or return the data here
        return "Web scraping successful."
    else:
        return "Failed to fetch the website."

# Function for sending email
def send_email(subject, message, to_email):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587
    sender_email = 'your_email@example.com'  # Replace with your email
    sender_password = 'your_password'  # Replace with your email password

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(sender_email, sender_password)

    email_message = f'Subject: {subject}\n\n{message}'
    server.sendmail(sender_email, to_email, email_message)

    server.quit()

def send_whatsapp_message(phone_number, message):
    # Use pywhatkit to send a WhatsApp message
    pywhatkit.sendwhatmsg(phone_number, message, datetime.datetime.now().hour,
                          datetime.datetime.now().minute + 2)  # Send the message after 2 minutes
    speak('WhatsApp is opening, and the message will be sent shortly.')

def my_assistant():
    global expecting_yes_no
    # Activate the initial greeting
    initial_greeting()

    # Cut-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()
        # if expecting_yes_no:
        #     handle_yes_no_response(my_request)
        #     continue

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
        elif 'what is the date and time' in my_request or 'what is the time and date' in my_request:
            ask_date_and_time()
            continue
        # elif 'okay' in my_request:
        #     respond_to_okay()
        #     continue
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
        elif 'send email' in my_request:
            # Replace the placeholders with actual subject, message, and recipient
            send_email('Subject', 'Message body', 'recipient@example.com')
            speak('The email has been sent.')
            continue
        elif 'web scraping' in my_request:
            # Replace the URL with the website you want to scrape
            scraped_data = scrape_website('https://www.example.com')
            speak(scraped_data)  # Speak the result to the user
            continue
        # Inside the my_assistant function, find the 'send whatsapp message' block and modify it:

        # Inside the my_assistant function, find the 'send whatsapp message' block and modify it as follows:

        elif 'send whatsapp message' in my_request:
            speak("Sure, who would you like to send the message to? Please say their name or phone number.")
            # Listen for and recognize the recipient's name or number
            recipient_info = transform_audio_into_text().lower()  # Convert the input to lowercase for case-insensitive matching
            recipient_phone_number = None  # Initialize recipient_phone_number to None

            if 'name' in recipient_info:
                speak("Please say the name or contact of the recipient.")
                recipient_name = transform_audio_into_text().lower()  # Convert the recipient's name to lowercase
                # Use the recipient's name to look up their phone number (you need to implement this part)
                recipient_phone_number = lookup_phone_number(recipient_name)
            elif 'number' in recipient_info:
                speak("Please say the phone number of the recipient.")
                recipient_phone_number = transform_audio_into_text()  # Listen for and recognize the recipient's phone number

            if recipient_phone_number:
                speak("What message would you like to send?")
                message = transform_audio_into_text()  # Listen for and recognize the message

                # Check if both recipient_phone_number and message are recognized
                if message:
                    send_whatsapp_message(recipient_phone_number, message)
                    continue
                else:
                    speak("Sorry, I couldn't understand the message. Please try again.")
            else:
                speak("Sorry, I couldn't understand the recipient's information. Please try again.")
                continue

        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break
        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break


my_assistant()



# speak("Hello Jim. I hope you have a nice day")










