import PySimpleGUI as sg
import zip_extractor as zip_ext

sg.theme("black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
button_choose1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select folder: ")
input2 = sg.Input()
button_choose2 = sg.FolderBrowse("Choose", key="folder")

decompress_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")


layout = [[label1, input1, button_choose1], [label2, input2, button_choose2], [decompress_button, output_label]]


window = sg.Window("Archive Extractor", layout=layout)
while True:

    event,values = window.read()
    archive_path = values["archive"]
    folder = values["folder"]
    zip_ext.extract_archive(archive_path, folder)
    window['output'].update(value="Extract the files successfully")

window.close()

