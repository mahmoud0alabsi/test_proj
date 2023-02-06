import streamlit as st

st.title("Give Me Questions & Answers")
st.header('Upload PDF File:')

st.text_input("Your text", key="textBox")
pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

st.success('PLease upload pdf file!')
