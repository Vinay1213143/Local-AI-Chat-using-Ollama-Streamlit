import streamlit as st
import ollama

st.set_page_config(page_title="Local AI Chat",layout="centered")

st.title("Local AI Chat using Ollama")

user_input=st.text_input("Write your Question:")

if st.button("Generate Answer"):
    if user_input.strip()=="":
        st.warning("Please enter aa question")
    else:
        response=ollama.chat(
            model='llama3.2:latest',
            messages=[
                {'role':'user','content':user_input}
            ]
        )

        st.subheader("Ollama Response")
        st.write(response['message']['content'])
        