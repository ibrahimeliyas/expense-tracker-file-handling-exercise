import json

FILE_NAME = "expenses.json"


def save_expenses(expenses):
    data = []

    for expense in expenses:
        data.append(expense.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []