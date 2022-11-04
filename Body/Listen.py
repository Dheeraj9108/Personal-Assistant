import pyaudio
import speech_recognition as sr
from googletrans import Translator

# Listening : Hindi or English

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='hi')
    except:
        return ""

    query = str(query).lower()
    return query

# print(Listen())

#Translation 

def TranslationHinToEnglish(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data =  result.text  # removing text from the result
    print(f"Yuo:{data}.")
    return data 

# TranslationHinToEnglish("मेरा नाम धीरज है")

# Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEnglish(query)
    return data

MicExecution()