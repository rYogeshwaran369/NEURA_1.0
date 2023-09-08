import speech_recognition as sr
import subprocess
import pyttsx3
import pyautogui
import time

name=""
def listen_and_recognize():
    global name
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
      if(len(name)==0):
            try:
                speak("Hi, I'm your Intelligence System.")
                speak("What's your name?")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                nameinput = recognizer.recognize_google(audio).lower()
                name = nameinput.strip()
                speak(f"Hello {name}, how can I help you?")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand your name. Please try again.")
            except sr.RequestError as e:
                speak(f"Sorry, there was an error recognizing your name. {e}")

      if(len(name)!=0):
            print("listening")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")

                if "open file explorer" in command:
                    open_file_explorer()
                elif "open disk" in command:
                    drive_letter = command.split()[-1]
                    open_disk(drive_letter)
                elif "open folder" in command:
                    folder_name = " ".join(command.split()[2:])
                    open_folder(folder_name)
                elif "open chrome" in command:
                    open_chrome()
                elif "search" in command:
                    search_query = " ".join(command.split()[1:])
                    search_in_chrome(search_query)
                elif "open code" in command:  
                    open_vscode()
                elif "create new file" in command:
                    create_html()
                elif "create h1 tag" in command:
                    create_h1()
                elif "run the code" in command:
                    run()
                elif "close" in command:
                    off()

                else:
                    speak(f"{command} Command not recognized")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results: {e}")


def off():
    try:
        pyautogui.hotkey('windows','d')
        time.sleep(1)
        pyautogui.hotkey('alt','f4')
        time.sleep(1)
        pyautogui.press('enter')
    except Exception as e:
        print(f"Error searching in Google Chrome: {e}")



def search_in_chrome(query):
    try:
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
        pyautogui.hotkey('ctrl', 't') 
        pyautogui.write(query) 
        pyautogui.press('enter')
        speak(f"Searching for {query} in Google Chrome")
    except Exception as e:
        print(f"Error searching in Google Chrome: {e}")


def open_vscode():
    try:
        subprocess.Popen(["C:\\Users\\waran\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd"])
        speak("Opening Visual Studio Code")
    except Exception as e:
        print(f"Error opening Visual Studio Code: {e}")

def create_html():
    try:
        speak("open new file")
        pyautogui.hotkey('ctrl','n')
        file_name = file_names()
        pyautogui.write(file_name+".html")
        pyautogui.hotkey('ctrl','s')
        time.sleep(1) 
        pyautogui.press('enter')
    except Exception as e:
        print(f"Error searching in Google Chrome: {e}")

def file_names():
     speak("what is your file name?")
     recognizer = sr.Recognizer()
     with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            file_name = recognizer.recognize_google(audio).lower()
        except Exception as e:
            speak("sorry can't understand, try again")
            file_names()
        return file_name
def create_h1():
    try:
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)
        pyautogui.press('delete')
        speak("give some title")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            title = recognizer.recognize_google(audio).lower()
            print("title")
            time.sleep(1)
            pyautogui.write(f'<h1>{title}</h1>')
    except Exception as e:
        print(f"Error searching in Google Chrome: {e}")
    

def run():
    try:
        pyautogui.hotkey('fn','f5')
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
    except Exception as e:
        print("executed")

def open_chrome():
    try:
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
        speak("Opening Chrome")
    except Exception as e:
        print(f"Error opening Microsoft Edge: {e}")

def open_file_explorer():
    try:
        subprocess.Popen(["explorer.exe"])
        speak("Opening File Explorer")
    except Exception as e:
        print(f"Error opening File Explorer: {e}")

def open_disk(drive_letter):
    try:
        subprocess.Popen([f'explorer.exe', f'{drive_letter}:\\'])
        speak(f"Opening Disk {drive_letter}")
    except Exception as e:
        print(f"Error opening Disk {drive_letter}:\\: {e}")

def open_folder(folder_name):
    try:
        subprocess.Popen([f'explorer.exe', f'{folder_name}'])
        speak(f"Opening Folder {folder_name}")
    except Exception as e:
        print(f"Error opening Folder {folder_name}: {e}")

def speak(message):
    print(message)
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        listen_and_recognize()