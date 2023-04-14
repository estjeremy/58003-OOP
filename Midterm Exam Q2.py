import tkinter as tk

# Function to convert cm to m and km
def convert():
    try:
        cm = float(entry_cm.get())
        m = cm / 100
        km = cm / 100000
        entry_m.delete(0, tk.END)
        entry_m.insert(0, str(m))
        entry_km.delete(0, tk.END)
        entry_km.insert(0, str(km))
    except ValueError:
        pass

# Create GUI
root = tk.Tk()
root.title("Length Converter")
root.geometry("500x250")

# Create Header Label
label_header = tk.Label(root, text="Metric Units of Length", font=("Arial", 10), pady=5)

# Create Labels
label_cm = tk.Label(root, text="Enter the distance in centimeters(cm):")
label_m = tk.Label(root, text="Conversion into meter (m):")
label_km = tk.Label(root, text="Conversion into Kilometers(km):")

# Create Entry Widgets
entry_cm = tk.Entry(root)
entry_m = tk.Entry(root)
entry_km = tk.Entry(root)

# Create Convert Button
button_convert = tk.Button(root, text="Convert", command=convert)

# Add Widgets to Grid
label_header.grid(row=0, column=0, columnspan=2)
label_cm.grid(row=1, column=0, sticky=tk.E)
entry_cm.grid(row=1, column=1, sticky=tk.W)
label_m.grid(row=2, column=0, sticky=tk.E)
entry_m.grid(row=2, column=1, sticky=tk.W)
label_km.grid(row=3, column=0, sticky=tk.E)
entry_km.grid(row=3, column=1, sticky=tk.W)
button_convert.grid(row=4, column=0, columnspan=2, pady=10)

# Center Widgets
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

# Start GUI
root.mainloop()
