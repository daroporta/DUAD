import PySimpleGUI as sg


def record_expenses(list_of_categories, list_of_income_and_expenses):
    layout = [[sg.Text("EXPENSES", font=80, justification="center", expand_x=True)],
            [sg.Text("Title:    "), sg.InputText(key="-TIT-")],
            [sg.Text("Amount:   "), sg.InputText(key="-AMT-")],
            [sg.Text("Category:   "), sg.InputText(key="-CAT-")], 
            [sg.Button("Save"), sg.Cancel(key="-CAN-")], 
            [sg.Text(key="-output-")]
    ]

    window= sg.Window("Expenses", layout)

    while True:
        event, values = window.read()
        expense_category, title, amount=values["-CAT-"].strip().capitalize(), values["-TIT-"].strip().capitalize(), values["-AMT-"].strip().capitalize()
        if event == sg.WIN_CLOSED or event =='Exit' or event == "-CAN-":
            break
        elif expense_category and title and amount:
            if expense_category in list_of_categories:
                new_income_expense={"category":expense_category,"type":"Expense", "title":title,"amount":amount}
                list_of_income_and_expenses.append(new_income_expense)
                window["-output-"].update(f"The expense has been added. {list_of_income_and_expenses}")
            else:      
                window["-output-"].update(f"The category: '{expense_category}' does not exist, try again. Your current list {list_of_income_and_expenses}")   
        else:
            window["-output-"].update(f"Please complete all the spaces. Your current list {list_of_income_and_expenses}") 
    window.close()


def record_income(list_of_categories, list_of_income_and_expenses):
    layout = [[sg.Text("INCOME", font=80, justification="center", expand_x=True)],
            [sg.Text("Title:    "), sg.InputText(key="-TIT-")],
            [sg.Text("Amount:   "), sg.InputText(key="-AMT-")],
            [sg.Text("Category:   "), sg.InputText(key="-CAT-")], 
            [sg.Button("Save"), sg.Cancel(key="-CAN-")], 
            [sg.Text(key="-output-")]
    ]

    window= sg.Window("Income", layout)

    while True:
        event, values = window.read()
        income_category, title, amount=values["-CAT-"].strip().capitalize(), values["-TIT-"].strip().capitalize(), values["-AMT-"].strip().capitalize()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == "-CAN-":
            break
        elif income_category and title and amount:
            if income_category in list_of_categories:
                new_income_expense={"category":income_category,"type":"Income", "title":title,"amount":amount}
                list_of_income_and_expenses.append(new_income_expense)
                window["-output-"].update(f"The expense has been added. {list_of_income_and_expenses}")
            else:      
                window["-output-"].update(f"The category: '{income_category}' does not exist, try again. Your current list {list_of_income_and_expenses}")   
        else:
            window["-output-"].update(f"Please complete all the spaces. Your current list {list_of_income_and_expenses}") 
    window.close()