import pyttsx3
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("speech-male/female")

title_label = Label(root,text = "Speech-male,female",font = "Times 15 bold",fg = "maroon")
title_label.pack(side = TOP)

user_input = StringVar()
screen = Entry(root,textvariable = user_input)
screen.update()
screen.pack()

male = 0
female = 1

def male_voice():
    x = user_input.get()
    speak(str(x),male)
    screen.update()

def female_voice():
    y = user_input.get()
    speak(str(y),female)
    screen.update()

def speak(audio,gender):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty("voice", voice[gender].id)
    engine.say(audio)
    engine.runAndWait()

male_button = Button(root,text="male",command = male_voice)
male_button.pack()

female_button = Button(root,text="female",command = female_voice)
female_button.pack()

root.mainloop()
