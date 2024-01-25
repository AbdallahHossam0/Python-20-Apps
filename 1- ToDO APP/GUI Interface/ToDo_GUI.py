import PySimpleGUI as sg
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBlue")

addButton = sg.Button("Add", size= 13, mouseover_colors="Blue")
inputBox = sg.Input(tooltip = "Enter the ToDo", key= "Add Text Box")
label = sg.Text("Type in the ToDo")

listBox = sg.Listbox(values= functions.getToDos("todos.txt"),
                     key= "ToDo List",
                     enable_events= True,
                     size = [45, 10])
editButton = sg.Button("Edit", mouseover_colors="Yellow")

completeButton = sg.Button("Complete", mouseover_colors="Green")

exitButton = sg.Button("Exit")

col1 = sg.Column([[editButton], [completeButton]])

window = sg.Window("My ToDO App", 
                   layout= [[label],
                            [inputBox, addButton], 
                            [listBox, col1],
                            [exitButton]],
                   font= ('Helvetica', 14))
while True:
    event , values = window.read() # * this is called structure binding in C++ -Multiple Values Assignment-
    
    match event:
        case "Add":
            todos = functions.getToDos("todos.txt")
            todos.append(values["Add Text Box"] + "\n")
            functions.writeToDos("todos.txt", todos)
            window['ToDo List'].update(todos)
        case "Edit":
            try:
                todoOld = values['ToDo List'][0] 
                todoNew = values['Add Text Box']+ '\n'

                todos = functions.getToDos("todos.txt")
                todos[todos.index(todoOld)] = todoNew
                functions.writeToDos("todos.txt", todos)
                window['ToDo List'].update(values= todos)
            except IndexError:
                sg.popup("Please, Select the ToDo you want to edit first.", text_color= "Red", title= "Error!!")
        case 'ToDo List':
            window['Add Text Box'].Update(values['ToDo List'][0])
        case "Complete":
            try:
                completedTodo = values['ToDo List'][0]
                todos = functions.getToDos("todos.txt")
                todos.remove(completedTodo)
                functions.writeToDos("todos.txt", todos)
                window['ToDo List'].update(values= todos)
                window["Add Text Box"].update(value= '')
            except IndexError:
                sg.popup("Please, Select the ToDo you want to complete first.", text_color= "Red", title= "Error!!")
        case sg.WIN_CLOSED | "Exit":
            break

window.close()

