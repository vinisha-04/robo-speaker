import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("robo speaker")
root.geometry("900x550+250+100")
root.resizable(False,False)
root.configure(bg="#8D6B94")


# code for robo speaker
obj = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    sex = gender.get()
    s = speed.get()
    vol = frequency.get()
    voices = obj.getProperty('voices')
    def setvoice():
        if(sex == 'Male'):
            obj.setProperty('voice',voices[0].id)
            obj.say(text)
            obj.runAndWait()
        else:
            obj.setProperty('voice', voices[1].id)
            obj.say(text)
            obj.runAndWait()
    if(text):
        if(s == "Fast"):
            obj.setProperty('rate',250)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()
        elif(s == "Normal"):
            obj.setProperty('rate',200)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()
        else:
            obj.setProperty('rate',150)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()

    '''if(text):
        if(vol == "High"):
            obj.setProperty("volume",1)
            setvoice()
        elif(vol == 'Medium'):
            obj.setProperty('volume',0.7)
            setvoice()
        elif(vol == 'Low'):
            obj.setProperty('volume',0.3)
            setvoice()
        else:
            obj.setProperty('volume',0)
            setvoice()'''



def download():
    text = text_area.get(1.0, END)
    sex = gender.get()
    s = speed.get()
    vol = frequency.get()
    voices = obj.getProperty('voices')

    def setvoice():
        if (sex == 'Male'):
            obj.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            obj.save_to_file(text,'text.mp3')
            obj.runAndWait()
        else:
            obj.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            obj.save_to_file(text,'text.mp3')
            obj.runAndWait()

    if (text):
        if (s == "Fast"):
            obj.setProperty('rate', 300)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()
        elif (s == "Normal"):
            obj.setProperty('rate', 250)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()
        else:
            obj.setProperty('rate', 150)
            if (vol == "High"):
                obj.setProperty("volume", 1)
                setvoice()
            elif (vol == 'Medium'):
                obj.setProperty('volume', 0.7)
                setvoice()
            elif (vol == 'Low'):
                obj.setProperty('volume', 0.3)
                setvoice()
            else:
                obj.setProperty('volume', 0)
                setvoice()



# f7cac9
#fff1e6
# FRAME
top_frame = Frame(root,bg = "#f6b89e",width=1000,height = 100)
top_frame.place(x=0,y=0)

logo = PhotoImage(file="C:\\Users\\Manoju vinisha\\OneDrive\\Desktop\\d1.png")
Label(top_frame,image=logo,bg="#f6b89e").place(x = 10 , y = 12)

# text on the frame
Label(top_frame,text="TEXT TO SPEECH",font='arial 20 bold',bg='#f6b89e',fg="black").place(x=100,y=30)

# text box
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x = 10, y = 120,width = 400,height = 250)

# label for voice
Label(root,text="VOICE",font="arial 15 bold",bg="#8D6B94",fg="white").place(x = 460,y = 165)

# combobox for voice
gender = Combobox(root,values=["Male","Famale"],font="arial 14",state='r',width=12)
gender.place(x=450,y=200)
gender.set("Male")

# label for speed
Label(root,text="SPEED",font="arial 15 bold",bg="#8D6B94",fg="white").place(x = 710,y = 165)

# combobox for voice
speed = Combobox(root,values=["Fast","Normal","Slow"],font="arial 14",state='r',width=12)
speed.place(x=700,y=200)
speed.set("Normal")

# icon
image_icon= PhotoImage(file ='C:\\Users\\Manoju vinisha\\OneDrive\\Desktop\\i1.png')
root.iconphoto(False,image_icon)

# speak button
icon = PhotoImage(file="C:\\Users\\Manoju vinisha\\OneDrive\\Desktop\\i2.png")
b = Button(root,text="Speak",compound=LEFT,image=icon ,width = 130,font = "arial 14 bold",command=speaknow)
b.place(x=450,y=310)

# save button
icon2 = PhotoImage(file="C:\\Users\\Manoju vinisha\\OneDrive\\Desktop\\save.png")
b1 = Button(root,text="Save",compound=LEFT,image=icon2 ,width = 130,font = "arial 14 bold",command=download)
b1.place(x = 130 , y = 400)

# frequency Combobox
frequency = Combobox(root,values=["High","Medium","Low","Mute"],font="arial 14",state='r',width=12)
frequency.place(x = 702 , y = 315)
frequency.set("Medium")

# label for voice
Label(root,text="Volume",font="arial 15 bold",bg="#8D6B94",fg="white").place(x = 710,y =282 )



root.mainloop()