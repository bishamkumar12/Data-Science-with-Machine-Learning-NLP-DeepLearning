import streamlit as st
import pandas as pd


st.title("Streamlit text input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ", 0, 100, 25)

st.write(f"Your age is {age}")


options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"You selected {choice}")

data= {
    "Name": ["Bhisham Kumar", "John", "Jake", "Jill"], 
    "Age": [25, 24, 35, 40],
    "City": ["Mithi", "New York", "UK", "Chhachhro"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

if name:
    st.write(f"Hello, Mr {name}")




uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)