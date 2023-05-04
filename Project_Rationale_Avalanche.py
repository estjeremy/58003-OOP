import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hamilton and Jefferson's Method Calculator")

# Define a function for validating numerical input
def validate_num_input(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False

# Create labels and entry widgets for inputting data
initial_investment_label = tk.Label(window, text="Initial Investment:")
initial_investment_label.grid(row=0, column=0, padx=5, pady=5)
initial_investment_entry = tk.Entry(window, validate="key", validatecommand=(window.register(validate_num_input), '%S'))
initial_investment_entry.grid(row=0, column=1, padx=5, pady=5)

expected_return_label = tk.Label(window, text="Expected Rate of Return (%):")
expected_return_label.grid(row=1, column=0, padx=5, pady=5)
expected_return_entry = tk.Entry(window, validate="key", validatecommand=(window.register(validate_num_input), '%S'))
expected_return_entry.grid(row=1, column=1, padx=5, pady=5)

num_years_label = tk.Label(window, text="Number of Years:")
num_years_label.grid(row=2, column=0, padx=5, pady=5)
num_years_entry = tk.Entry(window, validate="key", validatecommand=(window.register(validate_num_input), '%S'))
num_years_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a function for running the Hamilton and Jefferson's Method calculations
def calculate():
    initial_investment = float(initial_investment_entry.get())
    expected_return = float(expected_return_entry.get()) / 100
    num_years = int(num_years_entry.get())

    # Perform the Hamilton and Jefferson's Method calculations
    present_value_hamilton = initial_investment / ((1 + expected_return) ** num_years)
    present_value_jefferson = initial_investment * (1 - expected_return) ** num_years

    # Display the results in the result_text text box
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Present Value (Hamilton's Method): ${present_value_hamilton:,.2f}\n")
    result_text.insert(tk.END, f"Present Value (Jefferson's Method): ${present_value_jefferson:,.2f}")
    result_text.config(state='disabled')

    # Clear the entry widgets
    initial_investment_entry.delete(0, tk.END)
    expected_return_entry.delete(0, tk.END)
    num_years_entry.delete(0, tk.END)

# Create a button to run the calculations
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create a text box to display the results
result_text = tk.Text(window, height=2, width=50, state='disabled')
result_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()
