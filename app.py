from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
# load in environment variables
KEY = os.getenv("OPEN_API_KEY")
# create open ai client
client = OpenAI(
  api_key=KEY,)

def get_openai_response(question):    
    response =  client.chat.completions.create(
        messages=[
        {   "role": "user",
            "content": question,
        }],
        model="gpt-3.5-turbo",
        temperature=.5,
        max_tokens=50)

    text = response.choices[0].message.content
    return text
    

# streamlit app
st.set_page_config(page_title="Q/A Demo")
st.header("Langchain Application")
input = st.text_input("Input: ",key="input")
response = get_openai_response(input)

submit=st.button("Ask a question")
if submit:
    st.subheader("The response is")
    st.write(response)