from tkinter import *
import random


def change_color():
    # Generate a random RGB color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'

    # Change the background color of the second button
    button2.config(bg=color)


# Create the window
window = Tk()
window.geometry("300x200")
window.title("Button")

# Create a frame to hold the buttons
frame = Frame(window)
frame.pack(side=BOTTOM, pady=10)

# Create the buttons
button2 = Button(frame, text="Color", bg="white", fg="red")
button2.pack(side=LEFT, padx=5)

button1 = Button(frame, text="<---Click to change the color of the button", command=change_color)
button1.pack(side=LEFT, padx=5)

# Start the main loop
window.mainloop()
