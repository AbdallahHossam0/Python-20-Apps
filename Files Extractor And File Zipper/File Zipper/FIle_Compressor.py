import PySimpleGUI as sg
from filezipping import makeZip


label1 = sg.Text("Select files to Compress")
input1 = sg.Input(tooltip= "Enter the file paths separated by semi-colons")
chooseFilesButton = sg.FilesBrowse("Choose The Files", key= "files")

label2 = sg.Text("Select Destination Folder")
input2 = sg.Input(tooltip= "Enter the Destination Path")
chooseFolderButton = sg.FolderBrowse("Choose The Folder", key = "folder")

compressButton = sg.Button("Compress")
outputLabel = sg.Text(key= "output", text_color="green")

window = sg.Window("File Compressor", layout=[[label1, input1, chooseFilesButton], 
                                              [label2, input2, chooseFolderButton],
                                              [compressButton, outputLabel]])

while True:
    event, value = window.read()
    filepaths = value["files"].split(';')
    folder = value["folder"]
    makeZip(filepaths=filepaths, folder=folder)
    window["output"].update(value= "The compressed file generated successfully.")
    if event == sg.WIN_CLOSED:
        break

window.close()
