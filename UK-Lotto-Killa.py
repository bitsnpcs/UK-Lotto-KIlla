#!/usr/bin/env python

# Author  Jade Tang (2018) - https://github.com/bitsnpcs

from Tkinter import *
import random
import webbrowser

# change url to your desired url by editing line 10,11 or 12
url1 = 'http://www.google.co.uk'
url2 = 'https://en.wikipedia.org/wiki/Open-source_software'
url3 = 'https://www.github.com'

def OpenUrl1():
    webbrowser.open(url1)

def OpenUrl2():
    webbrowser.open(url2)

def OpenUrl3():
    webbrowser.open(url3)
    
def x():
    sampleList = random.sample(range(1, 60),6)
    print(sampleList)
    sampleRandomNumberListAsString = ', '.join(str(x) for x in sampleList)
    output.delete(1.0, END)
    output.insert(END, sampleRandomNumberListAsString)

window = Tk()
window.title("UK Lotto Killa")
window.geometry("242x242")

GUIFrame1=Frame(window)
GUIFrame1.grid(row=3, column=0, sticky=W)

GUIFrame2=Frame(window)
GUIFrame2.grid(row=4, column=0, sticky=W)

GUIFrame3=Frame(window)
GUIFrame3.grid(row=11, column=0, sticky=W)

l1 = Label(window, text="             UK Lotto Killa", font="bold")
l1.grid(row=1, column=0, sticky=W)
l2 = Label(window, text="  code by bitsnpcs & nandal (2018)", fg="grey", font="none 8")
l2.grid(row=13, column=0, sticky=W)

l3 = Label(GUIFrame1, text="        ")
l3.grid(row=3, column=0, sticky=W)
output = Text(GUIFrame1, width=23, height=1)
output.grid(row=3, column=1, sticky=W)

l3 = Label(window, text="     ")
l3.grid(row=4, column=0, sticky=W)
l3 = Label(window, text="     ")
l3.grid(row=0, column=0, sticky=W)
l3 = Label(window, text="     ")
l3.grid(row=10, column=0, sticky=W)
l3 = Label(window, text="     ")
l3.grid(row=6, column=0, sticky=W)
l3 = Label(window, text="     ")
l3.grid(row=12, column=0, sticky=W)

l3 = Label(window, text="                You have Options")
l3.grid(row=7, column=0, sticky=W)
l3 = Label(window, text="      Donate percentage of winnings.")
l3.grid(row=8, column=0, sticky=W)
l3 = Label(window, text="      Donate stake to favorite project.")
l3.grid(row=9, column=0, sticky=W)

l3 = Label(GUIFrame2, text="        ")
l3.grid(row=4, column=0, sticky=W)
Button(GUIFrame2, text="Generate Numbers", width=17, command = x).grid(row=4, column=1, sticky=W)

l3 = Label(GUIFrame3, text=" ")
l3.grid(row=11, column=0, sticky=W)
Button(GUIFrame3, text="Project 1", width=6, command=OpenUrl1).grid(row=11, column=1, sticky=W)
Button(GUIFrame3, text="Project 2", width=6, command=OpenUrl2).grid(row=11, column=2, sticky=W)
Button(GUIFrame3, text="Project 3", width=6, command=OpenUrl3).grid(row=11, column=3, sticky=W)

window.mainloop()
