# Windows based speak function

# Advantages :- fast , can work offline

# Disadvantages :- OverSpeaking not allowed , Less Voices

import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init("sapi5") # sapi5 in a windows api which helps to access the voices
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices',voices[0].id)
#     engine.setProperty('rate',170) # setting the voice rate 
#     print("")
#     print(f"You: {Text}.")
#     print()
#     engine.say(Text)
#     engine.runAndWait()


# Speak("Hellow sir")

# Chrome base speak function

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options() # mic, mute ...
chrome_options.add_argument("--log-level=3") # used to prevent selenium from printing tips and trics in the terminal
chrome_options.headless = False # -- maence chrome will open but it will not be visible to us
Path = "DataBase\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lenghtofText = len(str(Text))

    if lenghtofText == 0:
        pass
    else:
        print("")
        print(f"Ai: {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        sleep(2)
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lenghtofText>=30:
            sleep(4)
        elif lenghtofText>=40:
            sleep(6)
        elif lenghtofText>=55:
            sleep(8)
        elif lenghtofText>=70:
            sleep(10)
        elif lenghtofText>=100:
            sleep(13)
        elif lenghtofText>=120:
            sleep(14)
        else:
            sleep(2)


Speak("Hellow jarvis")

# Advantages :- Many voices , More clear, Overspeaking allowed
# Disadvantages :- Word limit , slow. 
