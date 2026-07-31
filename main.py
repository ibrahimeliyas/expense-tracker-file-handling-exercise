from expense import Expense
from storage import save_expenses, load_expenses

expenses = []

# Load old expenses
old_data = load_expenses()

for item in old_data:
    expense = Expense(
        item["amount"],
        item["category"],
        item["description"]
    )
    expenses.append(expense)


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Category")
    print("4. Delete Expense")
    print("5. Total Expenses")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":

        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")

        expense = Expense(amount, category, description)
        expenses.append(expense)

        save_expenses(expenses)

        print("Expense Added!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses.")

        else:
            for i, expense in enumerate(expenses):
                print(f"{i + 1}.")
                expense.display()

    elif choice == "3":

        category = input("Enter category: ")

        found = False

        for expense in expenses:
            if expense.category.lower() == category.lower():
                expense.display()
                found = True

        if not found:
            print("No expense found.")

    elif choice == "4":

        if len(expenses) == 0:
            print("Nothing to delete.")

        else:
            for i, expense in enumerate(expenses):
                print(f"{i + 1}. {expense.description}")

            number = int(input("Delete which expense? "))

            if 1 <= number <= len(expenses):
                expenses.pop(number - 1)
                save_expenses(expenses)
                print("Deleted!")
            else:
                print("Invalid number.")

    elif choice == "5":

        total = 0

        for expense in expenses:
            total += expense.amount

        print("Total Expense =", total)

    elif choice == "6":

        save_expenses(expenses)
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")