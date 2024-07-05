import PySimpleGUI as sg

from Bonus.parsers14 import convert
label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")


label2 = sg.Text("Enter inches; ")
input2 = sg.Input(key="inches")

compress_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")
exit_button = sg.Button("Exit", key="exit")

window = sg.Window("Convertor", layout=[
                                    [label1, input1],
                                    [label2, input2],
                                    [compress_button, exit_button, output_label]],
                  )
while True:
    event, values = window.read()
    print(values)
    print(event)
    if event == "exit" or event == sg.WIN_CLOSED:
        break
    if event == "Convert":
        result = convert(feet=float(values["feet"]), inches=float(values["inches"]))
        window["output"].update(value=f"{result} m")

window.close()