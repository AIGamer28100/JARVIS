import os
import speech_recognition as sr
from time import ctime
import time
from gtts import gTTS
from subprocess import call
import cv2, sys, numpy, os, time

password = '0123456789-='

#Function to Read out The DATA
def speak(data):
    print("Speaking")
    tts = gTTS(text=data , lang='en',slow=False)
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    print(data)
    
#Funtion to Listen the Input Audio
def listening(t):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            data=r.recognize_google(audio,language = "en",show_all=True)
    except (sr.UnknownValueError,LookupError):
        return listening(t)
    except sr.RequestError as e:
        speak('Network Error.')
        exit()
    print(data)
    return data


#Funtion To Process Input And Do Actions and Give out Respected Outputs
def jarvis():
    try:
        print("Listening")
        t=time.time()
        data = listening(t)
        else:
            if 'exit' in data or 'quit' in data or 'logout' in data:            
                return 'exit'
            elif 'music' in data:
                speak('Opening Wynk Music .')
                os.system("google-chrome --new-window https://wynk.in")
            elif 'open' in data:
                data=data.split(" ")
                print(data)
                speak('Opening : '+data[1])
                url="google-chrome --new-tab https://"+data[1]+".com"
                os.system(url)
            elif 'reboot' in data or 'restart' in data:
                if 'system' in data:
                    speak('Rebooting System')
                    os.system('reboot')
                else:
                    speak('do u want me to Reboot the system?')
                    data=listening(t)
                    if 'yes' in data or 'ya' in data or 'ofcourse' in data or 'definitely' in data:
                        speak('Rebooting System..')
                        os.system('reboot')
                    elif 'no' in data or 'not' in data:
                        speak('Ok done!')
                    else:
                        speak('Skiping Statement')
            elif 'power off' in data or 'poweroff' in data or 'shutdown' in data or 'shut down' in data:
                speak('do u want me to Shut down the system?')
                data=listening(t)
                if 'yes' in data or 'ya' in data or 'ofcourse' in data or 'definitely' in data:
                    speak('Shutting Down System.')
                    call('echo {} | sudo -S {}'.format(password,'poweroff'),shell=True)
                elif 'no' in data or 'not' in data or 'na' in data or 'cancel' in data:
                    speak('ok done!')
                else:
                    speak('Skiping Statement')
            else:
                data="You said : "+data
                speak(data)
        return 0
    except KeyboardInterrupt:
        speak('Key board Interrupted !!')
        speak('Exiting...')
        exit()   

r=sr.Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 4000
r.dynamic_energy_threshold = True

try:
    while True:
        re = jarvis()
        if re == 'exit':
            speak('Exiting...')
            exit()
except KeyboardInterrupt:
    speak('Key board Interrupted !!')
    speak('Exiting...')

