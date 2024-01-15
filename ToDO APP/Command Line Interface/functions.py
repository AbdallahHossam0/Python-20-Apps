def getToDos(filepath):
    """Function to get the todos stored in the file path"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    file.close()
    return todos

def writeToDos(filepath, todos):
    """Function to write the todos in the file path"""
    with open(filepath, 'w') as file:
        file.writelines(todos)
    file.close()

