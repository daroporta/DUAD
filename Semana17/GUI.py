import PySimpleGUI as sg
# layout = [ [sg.Text('Hello, world!')] ]
# window = sg.Window('Hello Example', layout)
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
# window.close()

import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
# ---------------------------------------------------------------------- CREATE A WINDOW -----------------------------------------------

import PySimpleGUI as sg

layout = [  [sg.Text('ROW 1'), sg.Button('Row 1 - #1'), sg.Checkbox('Row 1 - #2'), sg.Button('Row 1 - #3')],
            [sg.Text('ROW 2'), sg.Checkbox('Row 2 - #1'), sg.Checkbox('Row 2 - #2'), sg.Checkbox('Row 2 - #3')],
            [sg.Text('ROW 3'), sg.Button('Row 3 - #1'), sg.Button('Row 3 - #2')]  ]

window = sg.Window('Window Title', layout)

event, values = window.read()

window.close()
# ----------------------------------------------------------------------TABS--------------------

layout = [  [sg.Text('Network Tester', font='_ 20')],
            [sg.TabGroup([[
                sg.Tab('Send', [[sg.Text('Message to send:'), sg.Multiline(size=(60,10), key='-SEND-')]]),
                sg.Tab('Receive', [[sg.Text('Message Received'), sg.Multiline(size=(60,10), key='-RCV-')]])]])],
            [sg.Button('Send Message'), sg.Button('Exit')]  ]

window = sg.Window('My Network Tester', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Send Message':
        sg.popup('Sending:', values['-SEND-'])
        window['-RCV-'].update(values['-SEND-'])
window.close()

# ---------------------------------------------


text_name= sg.popup_get_text("Enter your name", title="Textbox")
print("Your name is:",text_name)

text_surname= sg.popup_get_text("Enter your surname", title="Textbox")
print("Your surname is:", text_surname)

selected_file=sg.popup_get_file("Selected a file", title="File selected")
print("File selected;", selected_file)

selected_folder=sg.popup_get_folder("Get folder", title="Folder selector")
print("Folder Selected:", selected_folder)

ch = sg.popup_yes_no("Do you want to continue?", title="YesNo")

ch1=sg.popup_ok_cancel("Continue → ok", "stop → cancel", title="okCancel")
print("You clicked: ", ch)

text_surname= sg.popup("Example of no title in the bar", no_titlebar=True)
sg.popup_no_titlebar('I do not have a titlebar.') 

date = sg.popup_get_date()
sg.popup(f'You entered {date}')


if sg.popup_yes_no('Do you want to exit?') == 'Yes':
    exit()

print('Continuing on...')

#-------------------------BOXES WITH MULTIPLE INPUTS AND PRINT OF THE INPUTS----------------------------------------------

layout=[
[sg.Text("Name   "), sg.Input(key="-AA-")],  
[sg.Text("Surname   "), sg.Input(key="-BB-")],
[sg.Text("Gender   "), sg.Input(key="-CC-")],
[sg.Text(key="-OUT-")],
[sg.OK(), sg.Exit()]
]

window=sg.Window("Turtle", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    out = values["-AA-"] + " " + values["-BB-"] + " " + values["-CC-"]
    window["-OUT-"].update(out)
    print(event, values)
window.close()

#-----------------------------------------

def signup_login():
    layout = [
        [sg.Text("Login/Signup")]
        [sg.Button("Login"), sg.Button("Signup")]
    ]

    window= sg.Window("Login/Signup", layout, finalize=True)

    while True:
        event, values = window.read()

        if event=="Login":
            login()

        if event == "Signup":
            signup()

        if event == None:
            break

def login():
    layout[
        [sg.Text("Username")],
        [sg.Input(key="-US-")],
        [sg.Text("Password")],
        [sg.Input(key="-PW-", password_char= "*")]
        [sg.Ok(), sg.Cancel()]
    ]

    window=sg.Window("login", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        username= values["-US-"]
        password= values["-PW-"]
        print(f"Username: {username}\nPassword: {password}\n--")
    window.close()

def signup():
    layout[
        [sg.Text("Username")],
        [sg.Input(key="-US-")],
        [sg.Text("Password")],
        [sg.Input(key="-PW-", password_char= "*")]
        [sg.Ok(), sg.Cancel()]
    ]

    window=sg.Window("Signup", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        username= values["-US-"]
        password= values["-PW-"]
        print(f"Username: {username}\nPassword: {password}\n--")
    window.close()


signup_login()

#--------------------------------------

names = ["Addition", "Subtraction", "multiplication", "division"]

lst=sg.Combo(names, font=("Arial Bold", 14),
size=(10,10), enable_events=True,
readonly=False)


layout= [
    [sg.Text("first number    "), sg.Input(key= "first_number")],
    [sg.Text("Second number    "), sg.Input(key= "second_number")],
    [sg.Button("Calculate"), sg.text("Result", key= "result")]
]

window=sg.Window("Calculator", layout, size=(400, 100))

while True:
    event, values =window.read()
    print(event, values)
    result=0

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Calculate":
        if values["combo"] == "Addition":
            result = int(values["first_number"]) + int(values["second_number"])
            window["result"].update(result)

    if event == "Calculate":
        if values["combo"] == "Subtraction":
            result = int(values["first_number"]) + int(values["second_number"])
            window["result"].update(result)

    if event == "Calculate":
        if values["combo"] == "multiplication":
            result = int(values["first_number"]) + int(values["second_number"])
            window["result"].update(result)

if event == "Calculate":
        if values["combo"] == "division":
            result = int(values["first_number"]) + int(values["second_number"])
            window["result"].update(result)

window.close()


#--------------------------------------


layout=[
    [sg.Text("Name     "), sg.Input(key="name")]
    [sg.Text("Surname     "), sg.Input(key="surname")]
    [sg.Text("Gender     "), sg.Checkbox("Male", key="male"),
    sg.Checkbox("Female", key="female")],
    [sg.Button("Saved"), sg.text("Result", key="result")]
]

window= sg.Window("EmployeesForm", layout, size=(400,125))

while True:
    event, values =window.read()
    print(event, values)

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    gender = ""
    x=0
    if values["male"]==True and values["female"]==True:
        window["result"].update("You can only choose 1 of the gender options")
        x=1
    if values["male"]==False and values["female"]==False:
        window["result"].update("You can only choose 1 of the gender options")
        x=1
    if values["male"]==True and values["female"]==False:
        gender = "Male"
    if values["male"]==False and values["female"]==True:
        gender= "Female"

    if event =="Saved" and x == 0:
        f = open("employees.txt", "a")
        f.write(f"{values["name"]}{values["surname"]}{gender}\n")
        window["result"].update("Saving completed!")
        gender=""
        f.close()
window.close()


#------------------------MULTIPLE WINDOWS AT THE SAME TIME-----------------------------------
layout1 = [[sg.Text('Window 1')],
        [sg.Input(key='-INPUT-')],
        [sg.Text(key='-TEXT-')],
        [sg.Button('Show on Win 2')]]

layout2 = [[sg.Text('Window 2')],
        [sg.Input(key='-INPUT-')],
        [sg.Text(key='-TEXT-')],
        [sg.Button('Show on Win 1')]]

window1 = sg.Window('Window 1', layout1, relative_location=(0,-180), finalize=True)
window2 = sg.Window('Window 2', layout2, finalize=True)

while True:  # The Event Looop
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break
    if window == window1:       # if button click on window 1, show text on window 2
        window2['-TEXT-'].update(values['-INPUT-'])
    else:                       # button was on window 2, so show text on window 1
        window1['-TEXT-'].update(values['-INPUT-'])

window1.close()
window2.close()


#-----------------------------SEND EMAIL TEMPLATE-----

layout = [[sg.Text('Send an Email', font='Default 18')],
        [sg.Text('From:', size=(8,1)), sg.Input(key='-EMAIL FROM-', size=(35,1))],
        [sg.Text('To:', size=(8,1)), sg.Input(key='-EMAIL TO-', size=(35,1))],
        [sg.Text('Subject:', size=(8,1)), sg.Input(key='-EMAIL SUBJECT-', size=(35,1))],
        [sg.Text('Mail login information', font='Default 18')],
        [sg.Text('User:', size=(8,1)), sg.Input(key='-USER-', size=(35,1))],
        [sg.Text('Password:', size=(8,1)), sg.Input(password_char='*', key='-PASSWORD-', size=(35,1))],
        [sg.Multiline('Type your message here', size=(60,10), key='-EMAIL TEXT-')],
        [sg.Button('Send'), sg.Button('Exit')]]

window = sg.Window('Send An Email', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
        
#-------------------------FOR ERRORS

def main():
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)

    layout = [  [sg.Text('My Window')],
                [sg.Input(k='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window['-O U T'].update(values['-IN-'])
    window.close()

def func():

    main()

func()

#-------------------------------------ALL ELEMENTS


use_custom_titlebar = True if sg.running_trinket() else False

def make_window(theme=None):

    NAME_SIZE = 23


    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    # NOTE that we're using our own LOCAL Menu element. It can be the standard Menubar or the PySimpleGUI MenubarCustom
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [[name('Text'), sg.Text('Text')],
                [name('Input'), sg.Input(s=15)],
                [name('Multiline'), sg.Multiline(s=(15,2))],
                [name('Output'), sg.Output(s=(15,2))],
                [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
                [name('Checkbox'), sg.Checkbox('Checkbox')],
                [name('Radio'), sg.Radio('Radio', 1)],
                [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
                [name('Button'), sg.Button('Button')],
                [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
                [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
                [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
                [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

    layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,40))],
                [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
                [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
                [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
                [name('Horizontal Separator'), sg.HSep()],
                [name('Vertical Separator'), sg.VSep()],
                [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
                [name('Column'), sg.Column([[sg.T(s=15)]])],
                [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
                [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
                [name('Push'), sg.Push(), sg.T('Pushed over')],
                [name('VPush'), sg.VPush()],
                [name('Sizer'), sg.Sizer(1,1)],
                [name('StatusBar'), sg.StatusBar('StatusBar')],
                [name('Sizegrip'), sg.Sizegrip()]  ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
            [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c', expand_x=True)],
            [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-', p=0)],
            [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window


window = make_window()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if values['-COMBO-'] != sg.theme():
        sg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        sg.set_options(use_custom_titlebar=use_custom_titlebar)
        window.close()
        window = make_window()
    if event == 'Edit Me':
        sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
window.close()