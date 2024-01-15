import functions
import time

def add():
    todo = input("Enter a todo ") + '\n'
    todos = functions.getToDos("todos.txt")
    todos.append(todo)
    functions.writeToDos("todos.txt", todos)


def show():
    todos = functions.getToDos("todos.txt")
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}", end = '')


def edit():
    try:
        todo_index = int(input("Enter the index of the todo you need to edit ")) - 1
        todos = functions.getToDos("todos.txt")
        print(f"You are going to edit {todos[todo_index]}", end='')
        newTodo = input("Enter the new todo ") + '\n'
        todos[todo_index] = newTodo
        functions.writeToDos("todos.txt", todos)
    except IndexError:
        print("The value doesn't match any todo")
    except ValueError:
        print("What you entered is not Valid")


def complete():
    try:
        index = int(input("Enter the index of the todo you want to complete ")) - 1
        todos = functions.getToDos("todos.txt")
        todo_completed = todos[index]
        todos.pop(index)
        print (f"todo: '{todo_completed.strip('\n')}' is removed from the todo list")
        functions.writeToDos("todos.txt", todos)
    except IndexError:
        print("The value doesn't match any todo")
    except ValueError:
        print("What you entered is not Valid")


def printTime():
    now = time.strftime("%d,%b %Y - %H:%M:%S")
    print(now)

if __name__ == "__main__":
    printTime()
    while True:
        command = input("Enter add, show, edit, complete or quit: ").lower().strip()
        match command:
            case "add":
                add()
            case "show":
                show()
            case "edit":
                edit()
            case "complete":
                complete()
            case "quit":
                break
            case _: print("Command is not Valid")
    print("BYE!!")


