import PySimpleGUI as sg
from lists import create_list_of_categories, create_list_of_income_and_expenses
from categories import save_category
from expenses_income import record_expenses, record_income
from table import print_list_of_transactions
from import_export_data import export_transactions_to_csv, import_transactions_from_csv, export_categories_to_csv, import_categories_from_csv, clear_categories_in_csv, clear_transactions_in_csv


def main(list_of_categories, list_of_income_and_expenses):
    import_categories_from_csv(list_of_categories, "categories.csv")
    import_transactions_from_csv(list_of_income_and_expenses, "transactions.csv")

    clear_transactions_in_csv("transactions.csv")
    clear_categories_in_csv("categories.csv")
    

    layout = [[sg.Text('Personal Finances', font=80, justification="center", expand_x=True)],
            [sg.Button("Category", expand_x=True, key="-CAT-")],
            [sg.Button("Income", expand_x=True, key="-IN-"), sg.Button("Expenses", expand_x=True, key="-EX-")], 
            [sg.Button("List of transactions", expand_x=True, key= "-LOT-")],
            [sg.Button("Exit", expand_x=True, key="-EXIT-")],
    ]


    window= sg.Window("Personal Finances", layout)

    while True:
        try:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Exit' or event == "-EXIT-":
                export_categories_to_csv(list_of_categories)
                export_transactions_to_csv(list_of_income_and_expenses)
                break

            if event == "-CAT-":
                save_category(list_of_categories)
            elif event == "-EX-":
                record_expenses(list_of_categories, list_of_income_and_expenses)
            elif event == "-IN-":
                record_income(list_of_categories, list_of_income_and_expenses)
            elif event == "-LOT-":
                print_list_of_transactions(list_of_categories, list_of_income_and_expenses)
        except Exception as ex:
            print("There was an error in the program")
            print(ex)


    window.close()


main(create_list_of_categories(), create_list_of_income_and_expenses())