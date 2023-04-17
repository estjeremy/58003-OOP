from tkinter import *

window = Tk()
window.geometry("300x150")
window.title("Father of Computer")

label = Label(window, text="Charles Babbage", fg="black", bg="lightblue", font=("Arial", 20), width=15, anchor="center", highlightthickness=3, highlightcolor="turquoise")
label.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
