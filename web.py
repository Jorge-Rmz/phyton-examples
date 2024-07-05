import streamlit as st
import Funtions.functions as funct

todos = funct.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    funct.write_todos(todos)

st.title("My todo App")

st.subheader("This is my todo app. ")
st.text("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state