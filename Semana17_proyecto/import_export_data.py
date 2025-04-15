import csv


def export_transactions_to_csv(list_of_income_and_expenses, filename="transactions.csv"):
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["category", "type", "title", "amount"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(list_of_income_and_expenses)
        print(f"Data was exported to {filename}")
    except Exception as ex:
        print(f"There was an error when exporting the data: {ex}")


def export_categories_to_csv(list_of_categories, filename="categories.csv"):
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["category"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(list_of_categories)
        print(f"Data was exported to {filename}")
    except Exception as ex:
        print(f"There was an error when exporting the data: {ex}")



def import_transactions_from_csv(list_of_income_and_expenses, filename="transactions.csv"):
    try:
        with open(filename, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                list_of_income_and_expenses.append(row)   
            return list_of_income_and_expenses
    except Exception as ex:
        print(f"There was an error when importing the data: {ex}")


def import_categories_from_csv(list_of_categories, filename="categories.csv"):
    try:
        with open(filename, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                list_of_categories.append(row)   
            return list_of_categories
    except Exception as ex:
        print(f"There was an error when importing the data: {ex}")




def clear_transactions_in_csv(filename="transactions.csv"):
    try:
        with open(filename, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["category", "type", "title", "amount"]) 
    except Exception as ex:
        print(f"Error found: {ex}")


def clear_categories_in_csv(filename="categories.csv"):
    try:
        with open(filename, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["category"]) 
    except Exception as ex:
        print(f"Error found: {ex}")

