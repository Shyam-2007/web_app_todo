
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todos.append(st.session_state['new_todo'] + "\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a simple todo app!")
st.write("this is a todo app that helps with productivity")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()
st.text_input(label="", placeholder="Enter a todo..", key="new_todo", on_change=add_todo)



