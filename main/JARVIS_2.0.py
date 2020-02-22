import tkinter as tk
import wolframalpha
import wikipedia
import speech_recognition as sr
from gtts import gTTS
import os
import text_to_speech as speech
from selenium import webdriver


#Create Master window for initialising assitsant's GUI

master=tk.Tk()



def speak(entry):
    
    '''Objective-To define a function speak which prompts user to input by voice
       Input- Entry widget of main window of assistant
       Result-Entry widget will be filled by the voice input by user
    '''    
    
    speech.speak("Input by your voice", "en")
    
    #SpeechRec initialize
    
    #Using Recogonizer class for recognizing input coice
    #Using Microphone class to recogonize input voice via device's microphone
    
    r=sr.Recognizer()
    mic=sr.Microphone()
    
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)


    getvoice= r.recognize_google(audio)
    print(getvoice)
    
    #Insert Voice input in Entry Widget of master window first by clearing filled text in the widget
    #Using delete function and Insert function
    
    entry.delete(0,tk.END)
    entry.insert(0,getvoice)
    


def search_text(entry):
    
    '''Objective-To define a function search_text() to search for a query based on user input
       Input- Entry widget of master window to obtain the text entry
       Result- The query will be resolved based on specific keywords in the inputtext
    '''   
    
    if "close window" in entry.get().lower():
        speech.speak("Closing Window","en")
        
        #Using destroy() function to close the active window
        
        master.destroy()

    elif "youtube" in entry.get().lower(): 
        text=entry.get()
        #Calling search_web() function
        search_web(text)    

    elif "open " in entry.get().lower():
        
        #Open Desktop Apps
        #Calling open application functions
        
        input_string=entry.get().lower()
        
        #Calling open_application function
        
        open_application(input_string)
            
    elif "tell me about " in entry.get().lower():
        
        #To search for some topic on wikipedia
        
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
        
        #For calculating mathematical functions or to know the current temperature of a place
        
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
    
    #creating child window over master window
    
    window = tk.Toplevel(master,height=100,width=300)
    window.title("Query Result ")
    
    #Displaying text as result on the child window
    
    T = tk.Text(window)
    T.pack()    
    T.insert(tk.END, "Your answer is :\n "+answer)
    
    #button 'close' to destroy the active child window
    
    button=tk.Button(window,text="close",command=lambda: destroy_window(window))
    button.pack()
    window.mainloop()
    
def destroy_window(window):
    
    '''Objective-To define function destroy_window() to close the acive window
        Input-child window object
        Result-The active child window will be closed
    '''
    
    window.destroy()
    answer="What can i do for you now ? "
    ass_speak(answer)

def ass_speak(answer):
    
    '''Objective-To define a function ass_speak to speak a specific text
       Input-String answer which will be output as voice
    '''
    
    speech.speak(answer,"en")


def search_web(text):
    
    '''Objective-To define a function search_web() to implement queries based on browsers
       Input- String text containing query
    '''
    
    #Intializing selenium webdriver and geckodriver for firefox
    
    
    driver = webdriver.Firefox() 
    driver.implicitly_wait(1) 
    driver.maximize_window()
    
    # To find the index of keyword 'youtube'
    
    indx = text.lower().split().index('youtube') 
    query = text.split()[indx + 1:]
    
    #To join query ahead of youtube word to perform execution
    #print('+'.join(query))  
    
    driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
    
    speech.speak("What can i do for you now?","en")


def open_application(input_string):
    
    '''Objective-To define a function open_application to open desktop apps using os library
       Input=string input_string
       Result=os Library opens the requested application
    '''
    
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
    
    #To create labels on the master window
    
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
    
    #To set the focus of input on the entry widget
    
    tentry.focus()
    
    #To make a voice button for voice input by user
    
    voice_button = tk.Button(master, text="Voice",command=lambda: speak(tentry))
    voice_button.grid(row=9,column=0)
    
    #To make a search button for performing the user queries 
    
    search_button = tk.Button(master, text="Search",command=lambda: search_text(tentry))
    search_button.grid(row=10,column=0)
    
    #delete() function to clear the already filled text in entry widget
    
    tentry.delete(0,tk.END)
    
    master.mainloop()
    

main()
