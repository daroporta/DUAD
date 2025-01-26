import PySimpleGUI as sg
from list_of_transactions import print_list_of_transactions
from categories import save_category
from income_and_expenses import record_expenses, record_income
from data_of_transactions import export_data, import_file, import_file_categories, export_data_of_categories
from lists import create_list



def main(list_of_categories, list_of_income_and_expenses):

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
                break

            if event == "-CAT-":
                import_file_categories("Saved_categories", list_of_categories)
                save_category(list_of_categories)
                export_data_of_categories("Saved_categories", list_of_categories, headers=["Categories"])
            elif event == "-EX-":
                import_file("Saved_transactions", list_of_income_and_expenses)
                record_expenses(list_of_categories, list_of_income_and_expenses)
                export_data("Saved_transactions", list_of_income_and_expenses, list_of_income_and_expenses[0].keys())
            elif event == "-IN-":
                import_file("Saved_transactions", list_of_income_and_expenses)
                record_income(list_of_categories, list_of_income_and_expenses)
                export_data("Saved_transactions", list_of_income_and_expenses, list_of_income_and_expenses[0].keys())
            elif event == "-LOT-":
                import_file("Saved_transactions", list_of_income_and_expenses)
                import_file_categories("Saved_categories", list_of_categories)
                print_list_of_transactions(list_of_categories, list_of_income_and_expenses)
        except Exception as ex:
            print("There was an error in the program")
            print(ex)
    

    window.close()


list_of_categories, list_of_income_and_expenses= create_list()

main(list_of_categories, list_of_income_and_expenses)