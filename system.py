import streamlit as st
from pyChatGPT import ChatGPT
from pypdf import PdfReader


def get_result_form_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    st = ""

    for page in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page]
        st += text.extract_text()

    temp_ar = 'اكتب اسئلة واجوبتها عن النص الثالي:\n'
    temp_en = 'Write questions and anwers on next text:\n'

    return (temp_en + st)
    

def get_result_form_text(txt):
    temp_ar = 'اكتب اسئلة واجوبتها عن النص الثالي:\n'
    temp_en = 'Write questions and anwers on next text:\n'
    
    return (temp_en + txt)
    

st.title("Give Me Questions & Answers")
st.header('Upload PDF File:')

st.text_input("Your text", key="textBox")
pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

if st.button('Submit'):
    if pdf_file is not None:
        final_ans = get_result_form_pdf(pdf_file)
        st.success(final_ans)
    elif (st.session_state.textBox != ""):
        final_ans = get_result_form_text(st.session_state.textBox)
        st.success(final_ans)
    else:
        st.success('PLease upload pdf file!')
