import PySimpleGUI as sg
import Extractor as ex



sg.theme("DarkBlue")

# Labels 
label1 = sg.Text("Select Achieve:  ")
label2 = sg.Text("Select Directory:")

outputLabel = sg.Text(key= "output", text_color= "green")

# Text Boxes
textBox1 = sg.Input()
textBox2 = sg.Input()

# Buttons
chooseButton1 = sg.FileBrowse("Choose", key= "archive")
chooseButton2 = sg.FolderBrowse("Choose", key= "folder")

extractButton = sg.Button("Extract")

# Window
window = sg.Window("Files Extractor",
                   layout= [[label1, textBox1, chooseButton1],
                            [label2, textBox2, chooseButton2],
                            [extractButton, outputLabel]])

while True:
    event, values = window.read()

    archivePath = values["archive"]
    folderPath = values["folder"]

    ex.extract(archivePath, folderPath)
    window["output"].update(value= "Extraction Done Successfully")
    if event == sg.WIN_CLOSED:
        break

window.close()
