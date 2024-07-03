import Funtions.functions as fun
import PySimpleGUI as sg

label = sg.Text('Type in a todo')

input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

windows = sg.Window('My to-do app',
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 20))

while True:
    event,values = windows.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fun.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            fun.write_todos(todos)
        case sg.WIN_CLOSED:
            break
windows.close()


