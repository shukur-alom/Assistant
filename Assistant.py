
import os,playsound,random,requests,json,datetime,time,wikipedia,webbrowser,pyautogui
import speech_recognition as sr
import win32com.client as wincl

speaker_number = 0 #num 0 = man , num 1 = girl
speak = wincl.Dispatch("SAPI.SpVoice")
vcs = speak.GetVoices()
speak.Voice
speak.SetVoice(vcs.Item(speaker_number))

def unknown(x,y):
   dat = datetime.datetime.now()
   file = open("Not find ans.txt",'a')
   file.write(f"Time: {dat.time()}, Date: {dat.date()}\n{x} : {y}\nCode: elif '{y}' in text2:\n\n")
   file.close()
def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak.speak("Good Morning!")

   elif hour>=12 and hour<18:
      speak.speak("Good Afternoon!")   

   else:
      speak.speak("Good Evening!")  
def poirisoi():
   if speaker_number == 1:
      speak.speak("I am elija Sir. Please tell me how may I help you")  
   elif speaker_number == 0:
      speak.speak("I am Ali Sir. Please tell me how may I help you")  
def webOpen(How_open,link):
   speak.speak(f"Opening {How_open}")
   webbrowser.open_new_tab(f"{link}")
wishMe()
poirisoi()
while True:
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("listining.........")
      audio = r.listen(source)
      try:
         text = r.recognize_google(audio)
         tt = str(text)    
         text2 =  tt.lower()
         print(f"you said : {text} ")

         if 'who am i' in text2 or 'my name' in text2:
            speak.speak("You are {Your name}") # your name

         elif 'who are you' in text2 or 'your name' in text2 or'who you' in text2:
            poirisoi()

         elif 'what is my father' in text2 or 'my father' in text2:
            speak.speak('Your father name is {Father name}') #your father name

         elif 'what is your father' in text2 or 'your father' in text2:
            speak.speak('{Your name} make me. i have no father. he is my crator') #your name

         elif 'what is your mother' in text2 or 'your mother' in text2:
            speak.speak('{Your name} make me. i have no mother. he is my crator') # your name

         elif 'what is my mother' in text2 or 'my mother' in text2:
            speak.speak('Your mother name is {Your mother name}') #your mother name
 

         elif 'what is my sister' in text2 or 'my sister' in text2:
            speak.speak('Your sister name is {your sister name}') #your sister name   



         elif 'today news' in text2 or 'news' in text2:
            print("News......")
            tt = datetime.datetime.now()
            rt = f"Date{tt.date()}, Time {tt.time()}, news"
            url = ('https://newsapi.org/v2/top-headlines?'
               'sources=bbc-sport&'
               'apiKey=49e391e7066c4158937096fb5e55fb5d')
            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            for i in range(0, 101):
               speak.speak(my_json['articles'][i]['title'])

         elif 'today date' in text2 or 'date' in text2:
            dt = datetime.datetime.now()
            h = f'Date {dt.date()}'
            speak.speak(h)
         
         elif 'hear me' in text2 or 'can you hear me' in text2:
               speak.speak("Yes , I can hear you")
         
         elif 'laugh for me' in text2 or 'can you laugh for me' in text2:
            speak.speak("No, I am sorry. i am virtual assistant")

         elif 'you do' in text2 or 'what should you do' in text2:
            speak.speak("Like a virtual assistant")
         elif 'you from' in text2 or 'what are you from' in text2:
            speak.speak("I am your virtual assistant. I live on Internet")

         elif 'what is ubuntu' in text2 or 'ubuntu' in text2:
            speak.speak("ubantu is operating system")

         elif 'what is windows' in text2 or 'windows' in text2:
            speak.speak("windows is operating system")

         elif 'text file' in text2 or 'text' in text2:
            er = text2.split(" ")
            for x in er:
               pass
            ty = sr.Recognizer()
            with sr.Microphone() as source:
               print("Say something on your text ...")
            audio = ty.listen(source)
            try:
               txt = open(f'{str(x)}.txt','a')
               textt = ty.recognize_google(audio)
               print(f"\nOn your text: {textt}\n")
               txt.write(f'{str(textt)}')
               txt.close()
               print("\n crate sacsessfully\n")
            except: pass
         
         elif 'what is book ' in text2:
            speak.speak('Book is best friend for all')

         elif 'what is light' in text2 or 'light' in text2:
            speak.speak('Light is a electric device')

         elif 'wish me' in text2 or 'wish' in text2 or 'me wish' in text2:
            wishMe()
            poirisoi()

         elif 'how are you' in text2 or 'how you' in text2:
            speak.speak("I am fine. and you ?")

         elif 'open youtube' in text2 or 'youtube' in text2:
            webOpen("Youtube",'https://www.youtube.com')

         elif 'open facebook' in text2 or 'facebook' in text2:
            webOpen("Facebook",'https://www.facebook.com/')

         elif 'open github' in text2 or 'github' in text2:
            webOpen("github",'https://github.com/')    
         
         elif 'lock my computer' in text2 or 'lock' in text2:
            pyautogui.moveTo(20,770)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(55,185)
            pyautogui.click()
            pyautogui.moveTo(55,260)
            time.sleep(1)
            pyautogui.click()   
         elif 'open skype' in text2 or'skype' in text2:
            pyautogui.moveTo(20,770)
            time.sleep(1)
            pyautogui.click()
            pyautogui.moveTo(400,290)
            time.sleep(1)
            pyautogui.click()
            pyautogui.click() 
         ######################### add new hare
         else:
            try:
               sagg = wikipedia.suggest(text2)
               ans3 = wikipedia.summary(sagg)
               speak.speak(ans3.split('\n')[0]) 
               unknown('Not my Detabase',text2)
            except:
               try:
                  ans = wikipedia.summary(text2)
                  speak.speak(ans.split('\n')[0])
                  unknown('Not my Detabase',text2)
               except:
                  try:  
                     sugg = wikipedia.suggest(text2)
                     sca=wikipedia.search(sugg)
                     ans2 = wikipedia.summary(str(sca[0]))
                     speak.speak(ans2.split('\n')[0])
                     unknown('Not my Detabase',text2)
                  except:
                     unknown('not found',text2)
                     pass
      except: 
         pass