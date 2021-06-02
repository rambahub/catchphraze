from tkinter import *
import random

from playsound import playsound
BEEPER = ('catchphrase.mp3', 'catchphrase_26_sec.mp3', 'catchphrase_15_sec.mp3')

# create window with button
root = Tk ()
root.geometry ('400x400')

#random word generator
with open ("Catchphrase-Words.txt", "r") as file:
    allText = file.read ()
    words = list (map (str, allText.splitlines ()))
    # print random string
    print (random.choice (words))

#define timer function:
def timer():
    playsound (random.choice (BEEPER))

#define myClick function:
def myClick():
    while timer is True:
        print (random.choice (words))
    label2.config(text=random.choice(words))



# create label
label = Label (root, text='''To earn points, make sure someone from your
team isn't caught holding the Catchphrase
game unit when the timer runs out!''', padx=50, pady=40)
label.pack ()

#create button
button = Button (root, text='Start/Next', padx=10, pady=20)
button.pack ()
button.config(command=lambda: [myClick (), timer ()])
button.config (font=('Ink Free', 20, 'bold'))
button.config (activebackground='#fffb1f')
button.config (fg='#50288C')

#word generator in the window
label2=Label(root, text=random.choice(words), padx=10, pady=10)
label2.config(font=('Monospace', 30, 'bold'))
label2.pack()


root.mainloop ()
