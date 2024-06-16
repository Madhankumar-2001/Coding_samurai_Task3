# Coding_samurai_Task3

**Task-3**
***************************
Project Title: Expense Tracker
***************************

## Overview

This project is a simple command-line expense tracker application in Python, designed to help users manage their expenses, categorize spending, and generate financial reports. It allows users to add expenses, list them, calculate total expenses over different time frames, and generate monthly reports.

### How to Run

1. **Clone the Repository:**
   git clone (repository-url)
   cd (repository-directory)


2. **Install Dependencies:**
   The script requires Python 3.x, which should be installed on your system.

3. **Run the Application:**
   python (filename).py


### Code Explanation

1. **Imports:**
   - `import json`: For saving and loading expense data in JSON format.
   - `import datetime`: For handling date and time-related operations.

2. **Global Variables:**
   - `expenses = []`: A list to store all expense records.

3. **Function to Add an Expense:**
   - `def add_expense(amount, category, description)`: Adds a new expense with the current date and time, amount, category, and description to the expenses list.

4. **Function to List All Expenses:**
   - `def list_expenses()`: Prints all recorded expenses in a readable format.

5. **Function to Calculate Total Expenses:**
   - `def calculate_total_expenses(time_frame)`: Calculates and prints the total expenses for the specified time frame (daily, weekly, or monthly).
     - Filters expenses based on the time frame by comparing the current date and the expense date.

6. **Function to Generate Monthly Report:**
   - `def monthly_report()`: Generates and prints a report summarizing total expenses by category for each month.

7. **Function to Save Expense Data:**
   - `def save_data(filename)`: Saves the current expenses list to a file in JSON format.

8. **Function to Load Expense Data:**
   - `def load_data(filename)`: Loads expense data from a file if it exists, otherwise initializes an empty list.

9. **Main Function:**
   - `def main()`: The main function that runs the application.
     - Loads existing expense data from `expenses.txt`.
     - Displays a menu of options for the user to choose from.
     - Handles user input for adding expenses, listing expenses, calculating total expenses, generating monthly reports, saving data, and exiting the application.
     - Calls the appropriate functions based on user input.

10. **Run the Main Function:**
    - `if __name__ == "__main__":`: Ensures the main function runs only when the script is executed directly.

### Features

- **Add Expense:** Allows users to add new expenses with details such as amount, category, and description.
- **List Expenses:** Displays all recorded expenses with details.
- **Calculate Total Expenses:** Calculates total expenses for daily, weekly, or monthly time frames.
- **Monthly Report:** Generates a report summarizing total expenses by category for each month.
- **Save and Load Data:** Saves expense data to a file and loads it upon application startup to ensure data persistence.

### Usage

1. **Add Expense:** Enter the amount, category, and description of the expense.
2. **List Expenses:** View all recorded expenses.
3. **Calculate Total Expenses:** Get the total expenses for a specified time frame (daily, weekly, monthly).
4. **Monthly Report:** Generate a report of monthly expenses categorized by type.
5. **Save Data:** Save the current expense data to a file.
6. **Exit:** Save the data and exit the application.

### Example

1. Add Expense
2. List Expenses
3. Calculate Total Expenses
4. Monthly Report
5. Save Data
6. Exit
Choose an option: 1
Enter amount: 100.0
Enter category: Food
Enter description: Lunch
Expense added successfully.

Choose an option: 2
Date: 2024-06-16 12:30:45, Amount: 100.0, Category: Food, Description: Lunch

Choose an option: 3
Enter time frame (daily/weekly/monthly): daily
Total expenses for daily: 100.0

Choose an option: 4
Month: 2024-06
  Category: Food, Total: 100.0

Choose an option: 6
Data saved. Exiting the application.
