# test_project.py
import pytest
from project import add_expense, add_income, view_summary, expenses, income

# Helper function to clear global lists before each test
@pytest.fixture(autouse=True)
def clear_data():
    expenses.clear()
    income.clear()

def test_add_expense():
    add_expense_entry = {'description': 'Groceries', 'amount': 50.0}
    expenses.append(add_expense_entry)
    assert len(expenses) == 1
    assert expenses[0]['description'] == 'Groceries'
    assert expenses[0]['amount'] == 50.0

def test_add_income():
    add_income_entry = {'description': 'Salary', 'amount': 500.0}
    income.append(add_income_entry)
    assert len(income) == 1
    assert income[0]['description'] == 'Salary'
    assert income[0]['amount'] == 500.0

def test_view_summary(capsys):
    # Add test data
    expenses.append({'description': 'Groceries', 'amount': 50.0})
    income.append({'description': 'Salary', 'amount': 500.0})

    # Call the function
    view_summary()

    # Capture printed output
    captured = capsys.readouterr()

    # Verify summary content
    assert "Total Income: $500.00" in captured.out
    assert "Total Expenses: $50.00" in captured.out
    assert "Balance: $450.00" in captured.out
