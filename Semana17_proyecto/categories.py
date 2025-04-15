import PySimpleGUI as sg


def save_category(list_of_categories):
    layout = [[sg.Text("Add Category", font=80, justification="center", expand_x=True)],
            [sg.Text("Name of category:   "), sg.InputText(key="-CAT-")], 
            [sg.Button("Save"), sg.Cancel(key="-CAN-")],
            [sg.Text(key="-output-")]
    ]

    window= sg.Window("Category", layout)

    while True:
        event, values = window.read()
        category = values ["-CAT-"].strip().capitalize()
        new_category = {"category":category}
        list_of_items= [item["category"] for item in list_of_categories]

        if event == sg.WIN_CLOSED or event =='Exit' or event == "-CAN-":
            break

        elif category in list_of_items:
            window["-output-"].update(f"The category: '{category}' already exists")
        elif category:
            list_of_categories.append(new_category)
            window["-output-"].update(f"The category: '{category}' has been added {list_of_categories}")
        else:
            window["-output-"].update("Please enter a category")

    window.close()