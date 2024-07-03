import Funtions.functions as func
import PySimpleGUI as sg

label = sg.Text('Type in a todo')

input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(func.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
# button_labels = ["Close", "Apply"]
layout = [[label], [input_box, add_button], [list_box, edit_button]]

windows = sg.Window('My to-do app',
                    layout=layout,
                    font=("Helvetica", 20))

while True:
    event, values = windows.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            func.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = func.get_todos()

            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            func.write_todos(todos)
            windows['todos'].update(values=todos)
        case "todos":
            windows['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
windows.close()
