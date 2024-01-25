import streamlit as st
import functions

def addTodo():
    todo = st.session_state["newTodo"] + "\n"
    todos = functions.getToDos("todos.txt")
    todos.append(todo)
    functions.writeToDos("todos.txt", todos)
    st.session_state["newTodo"] = ""

todos = functions.getToDos("todos.txt")

st.title("My Todo Webapp")
st.subheader("This is my Todo Webapp")
# st.write("This app is used to increase your productivity")


for todo in todos:
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.remove(todo)
        functions.writeToDos("todos.txt", todos)
        del st.session_state[todo]
        st.rerun()
        

st.text_input("", 
              placeholder= "Add a New Todo",
              on_change= addTodo,
              key= "newTodo")
