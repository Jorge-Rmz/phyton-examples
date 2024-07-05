import Funtions.functions as func
import PySimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text('', key='clock')
label = sg.Text('Type in a todo')

input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add to-do", key="Add")
list_box = sg.Listbox(func.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
# button_labels = ["Close", "Apply"]
layout = [[clock],[label], [input_box, add_button], [list_box, edit_button, complete_button],[exit_button]]

windows = sg.Window('My to-do app',
                    layout=layout,
                    font=("Helvetica", 14))

while True:
    event, values = windows.read(timeout=300)
    windows['clock'].update(value=time.strftime('%b %d %Y %H:%M:%S'))

    match event:
        case "Add":
            todos = func.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            func.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = func.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                func.write_todos(todos)
                windows['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select a item first", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = func.get_todos()
                todos.remove(todo_to_complete)
                func.write_todos(todos)
                windows['todos'].update(values=todos)
                windows['todo'].update(value='')
            except IndexError:
                sg.popup("Please, select a item first", font=("Helvetica", 14))
        case "todos":
            windows['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
windows.close()
