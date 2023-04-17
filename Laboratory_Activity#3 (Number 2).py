from tkinter import *

window = Tk()
window.geometry("400x300+20+10")
window.title("Text Field")

# Create a StringVar to hold the text value
text_var = StringVar()

# Adjusted the Entry widget's parameters
txt = Entry(window, textvariable=text_var, width=30)
txt.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
