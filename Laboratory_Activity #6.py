# Laboratory No.6

import tkinter as tk

# define the values to display in the table
values = ['a', 1, 2, 3, 4]
squared_values = ['a^2', 1**2, 2**2, 3**2, 4**2]
cubed_values = ['a^3', 1**3, 2**3, 3**3, 4**3]

# create the GUI
root = tk.Tk()
root.title("Table")

# create the rows of the table
for i in range(len(values)):
    # create a label for the value
    value_label = tk.Label(root, text="{}".format(values[i]), padx=10, pady=10, anchor="w")
    value_label.grid(row=i, column=0, sticky="w")

    # create a label for the squared value
    squared_label = tk.Label(root, text="{}".format(squared_values[i]), padx=10, pady=10, anchor="w")
    squared_label.grid(row=i, column=1, sticky="w")

    # create a label for the cubed value
    cubed_label = tk.Label(root, text="{}".format(cubed_values[i]), padx=10, pady=10, anchor="w")
    cubed_label.grid(row=i, column=2, sticky="w")

# run the GUI
root.mainloop()
