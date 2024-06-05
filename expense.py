import json
import datetime


expenses = []

def add_expense(amount, category, description):
    expense = {
        'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)

def list_expenses():
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def calculate_total_expenses(time_frame):
    total = 0
    now = datetime.datetime.now()
    for expense in expenses:
        expense_date = datetime.datetime.strptime(expense['date'], "%Y-%m-%d %H:%M:%S")
        if time_frame == 'daily' and (now - expense_date).days < 1:
            total += expense['amount']
        elif time_frame == 'weekly' and (now - expense_date).days < 7:
            total += expense['amount']
        elif time_frame == 'monthly' and (now - expense_date).days < 30:
            total += expense['amount']
    print(f"Total expenses for {time_frame}: {total}")

def monthly_report():
    report = {}
    for expense in expenses:
        month = expense['date'][:7]  # YYYY-MM
        if month not in report:
            report[month] = {}
        if expense['category'] not in report[month]:
            report[month][expense['category']] = 0
        report[month][expense['category']] += expense['amount']
    for month, categories in report.items():
        print(f"Month: {month}")
        for category, total in categories.items():
            print(f"  Category: {category}, Total: {total}")

def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_data(filename):
    global expenses
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def main():
    load_data('expenses.txt')
    while True:
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Monthly Report")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            time_frame = input("Enter time frame (daily/weekly/monthly): ")
            calculate_total_expenses(time_frame)
        elif choice == '4':
            monthly_report()
        elif choice == '5':
            save_data('expenses.txt')
        elif choice == '6':
            save_data('expenses.txt')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

