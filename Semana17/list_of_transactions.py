import PySimpleGUI as sg


def print_list_of_transactions(list_of_categories, list_of_income_and_expenses):
    values_of_table=[[transaction["category"], transaction["type"], transaction["title"], transaction["amount"]] for transaction in list_of_income_and_expenses if isinstance(transaction, dict)]
    headings_of_table= ["Category", "Type", "Title", "Amount"]
    layout_1 = [
        [sg.Text("TABLE OF TRANSACTIONS", font=("Helvetica", 20), justification="center", expand_x=True)],
        [sg.Table(values=values_of_table,
        headings=headings_of_table,
        auto_size_columns=True, 
        display_row_numbers=False,
        selected_row_colors="blue on yellow",
        justification="center")]


    ]

    layout_2= [
        [sg.Text("CATEGORIES", font=("Helvetica", 20), justification="center", expand_x=True)],
        [sg.Table(values=[[category] for category in list_of_categories], headings=["Categories"], 
        auto_size_columns=True, 
        display_row_numbers=False, 
        selected_row_colors="blue on yellow", 
        justification="center")]

    ]

    tabs = sg.TabGroup([[sg.Tab("Transactions",layout_1),
        sg.Tab("Categories", layout_2)],
        [sg.Button("Return")]
        ], tab_location="centertop")

    window= sg.Window("TABLE OF TRANSACTIONS", [[tabs]], resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Return":
            break

    window.close()


