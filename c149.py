# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:38:42 2022

@author: g_raj
"""

from tkinter import*
import random 

root=Tk()
root.title("word generator")
root.geometry("500x500")
label1=Label(root)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(list1[2:5])
def randomWord():
    random_no1=random.randint(1,26)
    random_no2=random.randint(1,26)
    random_no3=random.randint(1,26)
    random_no4=random.randint(1,26)
    random_no5=random.randint(1,26)
    random_letter1=list1[random_no1]
    random_letter2=list1[random_no2]
    random_letter3=list1[random_no3]
    random_letter4=list1[random_no4]
    random_letter5=list1[random_no5]
    label1["text"]=random_letter1+random_letter2+random_letter3+random_letter4+random_letter5
button1=Button(root, text="generate a random word",command=randomWord)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()