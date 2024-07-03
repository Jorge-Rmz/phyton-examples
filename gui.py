import PySimpleGUI as sg

label = sg.Text('Type in a todo')

input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

windows = sg.Window('My to-do app', layout=[[label], [input_box, add_button]])
windows.read()
windows.close()


