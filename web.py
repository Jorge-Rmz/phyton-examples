import streamlit as st
import Funtions.functions as funct

todos = funct.get_todos()


st.title("My todo App")

st.subheader("This is my todo app. ")
st.text("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo ", placeholder="Add new todo...")


