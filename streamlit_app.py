import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key='AIzaSyAfwSGdnep8hbM3KE7GzbsFuh6bOQu16AE')

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(Input,Image,prompt):
    response=model.generate_content([Input,Image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")
    
st.set_page_config(page_title=" WIE's INVOICE GENERATOR") 
st.sidebar.header("RoboBill")
st.sidebar.write("Made by IEE WIE")
st.sidebar.write("Poweres by google gemini ai")
st.header("RoboBill")
st.subheader("Manage your expense with Robot!")
input=st.text_input("What do you want me to do?",key="input")
uploaded_file= st.file_uploader("Choose an image.",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image =Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
submit=st.button("Let's go!")

input_prompt= """
You are an expert in reading invoices. We are going to upload an image of an invoice
and you will have to answer any question based on the uploaded invoice image. Make
sure to keep the font uniform and give the items list in a point-wise format.
At the end,make sure to repeat the name of our app"RoboBill" and ask the user to use it again."""
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)
    st.write("Thanks for visting!")


    


