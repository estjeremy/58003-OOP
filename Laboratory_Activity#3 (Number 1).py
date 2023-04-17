import tkinter as tk

root = tk.Tk()
root.title("Label")

# Create a label widget for "Laboratory Activity 5" and "Submitted to: Mam Sa'yo"
label = tk.Label(root, text="Laboratory Activity 5\nSubmitted to: Mam Sayo", font=("Arial", 9))

# Place the label widget at the bottom of the window
label.pack(side=tk.BOTTOM, pady=50)

# Start the main event loop
root.mainloop()