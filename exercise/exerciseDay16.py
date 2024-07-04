import PySimpleGUI as sg

from Bonus.parsers14 import convert
label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")


label2 = sg.Text("Enter inches; ")
input2 = sg.Input(key="inches")

compress_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")

window = sg.Window("Convertor", layout=[
                                    [label1, input1],
                                    [label2, input2],
                                    [compress_button, output_label]],
                  )
while True:
    event, values = window.read()
    print(values)
    result = convert(feet=int(values["feet"]), inches=int(values["inches"]))
    print(result)
    window["output"].update(value=f"{result} m")

window.close()