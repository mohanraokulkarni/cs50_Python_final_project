import os
from tkinter import Tk, Label, Entry, Button, Listbox, Frame, END, messagebox

# Global lists to store expenses and income
expenses = []
income = []

# Function to add expense
def add_expense():
    description = expense_desc_entry.get()
    try:
        amount = float(expense_amount_entry.get())
        expenses.append({'description': description, 'amount': amount})
        expense_listbox.insert(END, f"Expense: {description} - ${amount:.2f}")
        expense_desc_entry.delete(0, END)
        expense_amount_entry.delete(0, END)
        messagebox.showinfo("Success", "Expense added successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount! Please enter a number.")

# Function to add income
def add_income():
    description = income_desc_entry.get()
    try:
        amount = float(income_amount_entry.get())
        income.append({'description': description, 'amount': amount})
        income_listbox.insert(END, f"Income: {description} - ${amount:.2f}")
        income_desc_entry.delete(0, END)
        income_amount_entry.delete(0, END)
        messagebox.showinfo("Success", "Income added successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount! Please enter a number.")

# Function to view summary
def view_summary():
    total_expenses = sum(item['amount'] for item in expenses)
    total_income = sum(item['amount'] for item in income)
    balance = total_income - total_expenses
    summary_message = (
        f"Total Income: ${total_income:.2f}\n"
        f"Total Expenses: ${total_expenses:.2f}\n"
        f"Balance: ${balance:.2f}"
    )
    messagebox.showinfo("Summary", summary_message)

# Function to save data to a file
def save_data():
    with open('budget_data.txt', 'w') as file:
        for item in income:
            file.write(f"INCOME,{item['description']},{item['amount']}\n")
        for item in expenses:
            file.write(f"EXPENSE,{item['description']},{item['amount']}\n")
    messagebox.showinfo("Save", "Data saved successfully.")

# Function to load data from a file
def load_data():
    if not os.path.exists('budget_data.txt'):
        return
    with open('budget_data.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == 'INCOME':
                income.append({'description': parts[1], 'amount': float(parts[2])})
                income_listbox.insert(END, f"Income: {parts[1]} - ${float(parts[2]):.2f}")
            elif parts[0] == 'EXPENSE':
                expenses.append({'description': parts[1], 'amount': float(parts[2])})
                expense_listbox.insert(END, f"Expense: {parts[1]} - ${float(parts[2]):.2f}")

# Creating the main application window
root = Tk()
root.title("Personal Finance Tracker")
root.configure(bg="#f0f0f0")  # Background color for the main window

# Make the root window resizable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Define color palette
bg_color = "#e6f7ff"
frame_color = "#b3e0ff"
button_color = "#99ccff"
text_color = "#003366"

# Income Frame
income_frame = Frame(root, bg=frame_color, bd=2, relief="groove")
income_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
income_frame.grid_rowconfigure(4, weight=1)  # Allow listbox to expand
income_frame.grid_columnconfigure(1, weight=1)

income_label = Label(income_frame, text="Add Income", bg=frame_color, fg=text_color, font=("Arial", 14, "bold"))
income_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

income_desc_label = Label(income_frame, text="Description", bg=frame_color, fg=text_color)
income_desc_label.grid(row=1, column=0, sticky="w")
income_desc_entry = Entry(income_frame)
income_desc_entry.grid(row=1, column=1, sticky="ew")

income_amount_label = Label(income_frame, text="Amount", bg=frame_color, fg=text_color)
income_amount_label.grid(row=2, column=0, sticky="w")
income_amount_entry = Entry(income_frame)
income_amount_entry.grid(row=2, column=1, sticky="ew")

income_button = Button(income_frame, text="Add Income", bg=button_color, command=add_income)
income_button.grid(row=3, column=0, columnspan=2, pady=5)

income_listbox = Listbox(income_frame, bg=bg_color)
income_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Expense Frame
expense_frame = Frame(root, bg=frame_color, bd=2, relief="groove")
expense_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
expense_frame.grid_rowconfigure(4, weight=1)  # Allow listbox to expand
expense_frame.grid_columnconfigure(1, weight=1)

expense_label = Label(expense_frame, text="Add Expense", bg=frame_color, fg=text_color, font=("Arial", 14, "bold"))
expense_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

expense_desc_label = Label(expense_frame, text="Description", bg=frame_color, fg=text_color)
expense_desc_label.grid(row=1, column=0, sticky="w")
expense_desc_entry = Entry(expense_frame)
expense_desc_entry.grid(row=1, column=1, sticky="ew")

expense_amount_label = Label(expense_frame, text="Amount", bg=frame_color, fg=text_color)
expense_amount_label.grid(row=2, column=0, sticky="w")
expense_amount_entry = Entry(expense_frame)
expense_amount_entry.grid(row=2, column=1, sticky="ew")

expense_button = Button(expense_frame, text="Add Expense", bg=button_color, command=add_expense)
expense_button.grid(row=3, column=0, columnspan=2, pady=5)

expense_listbox = Listbox(expense_frame, bg=bg_color)
expense_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Summary and Save Frame
summary_frame = Frame(root, bg=bg_color, bd=2, relief="groove")
summary_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
summary_frame.grid_columnconfigure(0, weight=1)
summary_frame.grid_columnconfigure(1, weight=1)

summary_button = Button(summary_frame, text="View Summary", bg=button_color, command=view_summary)
summary_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

save_button = Button(summary_frame, text="Save Data", bg=button_color, command=save_data)
save_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Load data at startup
load_data()

# Run the application
root.mainloop()
