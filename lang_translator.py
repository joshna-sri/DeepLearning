from tkinter import *

# Creating a GUI Window
window = Tk()
window.title("Language Translator")
window.geometry("1000x1000")

#global e2_value
def lang_translator():
    Dictionary = {"English": ["food", "travel", "speak"],
                  "Telugu": ["Aaharam", "Prayaṇaṁ", "Māṭlāḍatāru"],
                  "Tamil": ["Uṇavu", "Payaṇam", "Pēcu"],
                  "Malayalam": ["bhakshanam", "yaathra", "samsaarikkuka"],
                  "Kannada": ["AhAra", "PrayAṇa", "Mātanāḍuttāre"]}
    #for key , val in Dictionary.items():
#        for i in val:
    #if e2_value == Dictionary["English"][0]:
    global e2_value
    if e2_value == "food":
            telugu = Dictionary["Telugu"][0]
            tamil = Dictionary["Tamil"][0]
            malayalam = Dictionary["Malayalam"][0]
            kannada = Dictionary["Kannada"][0]
            t1.delete("1.0", END)
            t1.insert(END, telugu)
            t2.delete("1.0", END)
            t2.insert(END, tamil)
            t3.delete("1.0", END)
            t3.insert(END, malayalam)
            t4.delete("1.0", END)
            t4.insert(END, kannada)


e1 = Label(window, text="Input the word in English")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)


e3 = Label(window, text="Telugu")
e4 = Label(window, text="English")
e5 = Label(window, text="Malayalam")
e6 = Label(window, text="Kannada")

t1 = Text(window, height=5, width=20)
t2 = Text(window, height=5, width=20)
t3 = Text(window, height=5, width=20)
t4 = Text(window, height=5, width=20)

b1 = Button(window, text="Translate", command=lang_translator)
#radio_btn =Radiobutton (window, command=Lang_translator)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1,column=3)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
b1.grid(row=0, column=2)

window.mainloop()