import tkinter
from  tkinter import ttk
from tkinter import *

def translate(initial ,translated):
    label3 = ttk.label(text="translated_word",background="magenta",foreground ="blue" )
    label3.grid(row=1,column =0)


root = Tk()
frm = ttk.Frame(root, padding =10)

initial = StringVar()

label1 =ttk.Label(frm, text="Welcome",background="magenta",foreground ="blue")
label2 = Entry(root,textvariable=initial )
b = ttk.Button(frm, text="Translate",command= translate )
label1.grid(row =0, column =1)
label2.grid(row =0, column =2)

root.mainloop()


