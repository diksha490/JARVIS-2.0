import tkinter as tk
import wolframalpha
import wikipedia
import speech_recognition as sr
from gtts import gTTS
import os
import text_to_speech as speech
from selenium import webdriver


getvoice=""

#wolframalpha client

master=tk.Tk()

def speak(entry):
    
    speech.speak("Input by your voice", "en")
    #SpeechRec initialize
    r=sr.Recognizer()
    mic=sr.Microphone()
    
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)


    getvoice= r.recognize_google(audio)
    print(getvoice)
    entry.delete(0,tk.END)
    entry.insert(0,getvoice)
    


def search_text(entry):

    if "close window" in entry.get().lower():
        speech.speak("Closing Window","en")
        master.destroy()

    elif "youtube" in entry.get().lower():        
        #Search youtube using selenium and geckodriver
        text=entry.get()
        search_web(text)    

    elif "open " in entry.get().lower():
        
        #Open Desktop Apps
        #Calling open application functions
        input_string=entry.get().lower()
        open_application(input_string)
            
    elif "tell me about " in entry.get().lower():
        
        try:
            answer=wikipedia.summary(entry.get(),sentences=5)
            #calling Result Display Function
            Result_Display(answer)
            
        except:
            answer="I am Sorry , could not find the answer"
            speech.speak(answer,"en")
            #calling Result Display Function
            Result_Display(answer)
            

    elif "calculate" or "solve" or "temperature" in entry.get().lower():
        
        try:
            #Wolframalpha search
            client=wolframalpha.Client("U2WEAW-XVJ47X33XK")
            input_text=entry.get()
            result=client.query(input_text)
            answer=next(result.results).text
            speech.speak("Your answer is \n"+answer,"en")
            #calling Result Display Function
            Result_Display(answer)
            
        except:
            answer="I am Sorry , could not find the answer"
            speech.speak(answer,"en")
            #calling Result Display Function
            Result_Display(answer)
            
    
           

def Result_Display(answer):
    #creating child window    
    window = tk.Toplevel(master,height=100,width=300)
    window.title("Query Result ")
    
    #Displaying text as result    
    T = tk.Text(window)
    T.pack()    
    T.insert(tk.END, "Your answer is :\n "+answer)
    button=tk.Button(window,text="close",command=lambda: destroy_window(window))
    button.pack()
    window.mainloop()
    
def destroy_window(window):
    window.destroy()
    answer="What can i do for you now ? "
    ass_speak(answer)

def ass_speak(answer):
    speech.speak(answer,"en")


def search_web(text):
    #Search using selenium webdriver and geckodriver for firefox
    print(text)
    driver = webdriver.Firefox() 
    driver.implicitly_wait(1) 
    driver.maximize_window()

    indx = text.lower().split().index('youtube') 
    query = text.split()[indx + 1:]
    print('+'.join(query))    
    driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
    speech.speak("What can i do for you now?","en")


def open_application(input_string):
    
    try:
        if "excel" in input_string:
            speech.speak("Opening Microsoft Excel ","en") 
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk")
            
        elif "word" in input_string:
            speech.speak("Opening Microsoft Word ","en") 
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk")
            
        elif "powerpoint" in input_string:
            speech.speak("Opening Microsoft Power Point","en") 
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk")
            
        elif "firefox" in input_string or "mozilla" in input_string:
            speech.speak("Opening Mozilla Firefox","en") 
            os.startfile(r"C:\Users\Public\Desktop\Firefox.lnk")
            
        elif "opera" in input_string:
            speech.speak("Opening Opera browser","en") 
            os.startfile(r"C:\Users\saurabh\AppData\Local\Programs\Opera\launcher.exe")            
        speech.speak("What can i do for you now?","en")
        
    except:
        answer="Can not open the app "
        speech.speak(answer,"en")
        Result_Display(answer)
        
        
def main():
    master.title("Welcome Human ! ")
    
    #Label
    w=tk.Label(master,text="\nWhat do you want ?\n\n1. Say Calculate or Solve Mathematical Problem--",width=50)
    w.grid(row=0,column=0)
    w1=tk.Label(master,text="2. Say Tell Me about something on Wikipedia-----")
    w1.grid(row=1,column=0)
    w2=tk.Label(master,text="3. Say Play Youtube your favourite topic----------")
    w2.grid(row=2,column=0)
    w3=tk.Label(master,text="4. Say Open Microsoft-app to open---------------")
    w3.grid(row=3,column=0)
    w4=tk.Label(master,text="5. Say Open-Firefox for browsing on mozilla------")
    w4.grid(row=4,column=0)
    w5=tk.Label(master,text="6. Say Open-Opera for browsing on Opera--------")
    w5.grid(row=5,column=0)
    w6=tk.Label(master,text="7. Say Temperature-of-Place to know temperature\n")
    w6.grid(row=6,column=0)
    #Welcome Note
    speech.speak("Welcome Human ", "en")
    speech.speak("What do you want me to do ? ", "en")
    
    #Entry
    tentry=tk.Entry(master,width=50)
    tentry.grid(row=7,column=0)
    tentry.bind('<Return>',lambda event: OnPressReturn(str(tentry.get())))
    
    tentry.focus()
    
    voice_button = tk.Button(master, text="Voice",command=lambda: speak(tentry))
    voice_button.grid(row=9,column=0)

    search_button = tk.Button(master, text="Search",command=lambda: search_text(tentry))
    search_button.grid(row=10,column=0)
    
    tentry.delete(0,tk.END)
    
    master.mainloop()
    

main()
