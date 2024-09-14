# cs50_Python_final_project

🧾 Simple Budget Tracker

 Video Demo: [[URL HERE](https://youtu.be/f6C_qZzElM0)]
📄 Description:

The **Simple Budget Tracker** is a command-line Python application that helps you manage your personal finances by adding expenses, recording income, and viewing a summary of your financial status. The project uses file I/O operations to save and load data, ensuring your records persist between program runs. 🗂️

✨ Features

- 💸 Add Expense: Record an expense with a description and amount.
- 💰 Add Income: Add income entries with a description and amount.
- 📊 View Summary: Display total income, total expenses, and the current balance.
- 💾 Save Data: Save your income and expense entries to a text file (`budget_data.txt`) for future use.
- 📂 Load Data: Automatically load saved data from `budget_data.txt` when the program starts.

🛠️ How to Use

1. Run the Program: Execute `project.py` using Python.
   python project.py
2. Menu Options: The program presents a simple text-based menu with four options:
   - ➕ Add an Expense: Enter a description and amount for an expense.
   - ➕ Add Income: Enter a description and amount for an income.
   - 📋 View Summary: Display total income, total expenses, and balance.
   - 💾 Save and Exit: Save all data to `budget_data.txt` and exit the program.

3. Saving Data: When you select "Save and Exit," the program writes all income and expenses to `budget_data.txt` for future use. 📂

## 📂 Project Structure

- `project.py`: The main file containing the core logic of the budget tracker. It includes:
  - 🏁 `main()`: Provides a menu for interacting with the program.
  - 💸 `add_expense()`: Prompts the user for an expense description and amount, then stores it in a list.
  - 💰 `add_income()`: Prompts the user for an income description and amount, then stores it in a list.
  - 📊 `view_summary()`: Calculates and displays the total income, expenses, and balance.
  - 💾 `save_data()`: Saves the current income and expense data to a text file.
  - 📂 `load_data()`: Loads saved data from a text file when the program starts.

- `test_project.py`: Contains automated tests for the main functions using `pytest`. It includes:
  - 🧪 `test_add_expense()`: Tests adding an expense to the list.
  - 🧪 `test_add_income()`: Tests adding income to the list.
  - 🧪 `test_view_summary()`: Tests the summary output using `capsys` to capture printed output.

- `requirements.txt`: Lists required libraries for running tests. In this project, it includes `pytest`. 📋

🧪 Testing

This project uses the `pytest` framework to test core functions. To run the tests, execute the following

command:pytest test_project.py

The tests ensure that expenses and income are correctly added and that the summary displays accurate financial information. ✔️

🧩 Design Choices

- Data Persistence: The project uses a text file (`budget_data.txt`) for simple data storage. This choice allows for easy implementation and demonstration of file handling in Python. 🗄️
- Testing: The use of `pytest` helps validate the functionality of adding expenses, income, and viewing the summary, ensuring the reliability of core features. 🧪
- User Interface: A command-line interface was chosen for simplicity and ease of use. Enhancements can be made in the future to include a graphical interface using libraries like Tkinter. 🖥️

🚀 Future Enhancements

🖼️ Add a graphical user interface (GUI) for a more user-friendly experience.
🗂️ Implement additional features such as expense categories and monthly budgeting.
📊 Allow data export to formats like CSV for external analysis.

📋 Requirements

🐍 Python 3.x
🧪 `pytest` for testing (listed in `requirements.txt`)

🏃 How to Run

1. Clone or download the project to your local machine. 💻
2. Navigate to the project's root directory.
3. Run the program:python project.py
4. Follow the on-screen prompts to add income, expenses, and view your summary.

Feel free to explore and extend the project as needed! 🎉
