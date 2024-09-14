# project.py
import os

# Global lists to store expenses and income
expenses = []
income = []

def main():
    # Load data if available
    load_data()

    while True:
        print("\nSimple Budget Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Summary")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            add_income()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            save_data()
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

def add_expense():
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: "))
        expenses.append({'description': description, 'amount': amount})
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def add_income():
    description = input("Enter income description: ")
    try:
        amount = float(input("Enter income amount: "))
        income.append({'description': description, 'amount': amount})
        print("Income added successfully.")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_summary():
    total_expenses = sum(item['amount'] for item in expenses)
    total_income = sum(item['amount'] for item in income)
    balance = total_income - total_expenses

    print("\n--- Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

def save_data():
    with open('budget_data.txt', 'w') as file:
        for item in income:
            file.write(f"INCOME,{item['description']},{item['amount']}\n")
        for item in expenses:
            file.write(f"EXPENSE,{item['description']},{item['amount']}\n")

def load_data():
    if not os.path.exists('budget_data.txt'):
        return
    with open('budget_data.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == 'INCOME':
                income.append({'description': parts[1], 'amount': float(parts[2])})
            elif parts[0] == 'EXPENSE':
                expenses.append({'description': parts[1], 'amount': float(parts[2])})

if __name__ == "__main__":
    main()
