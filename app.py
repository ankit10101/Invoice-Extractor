from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import os
from PIL import Image

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_gemini_response(image,prompt):
    response = model.generate_content([image,prompt])
    return response.text

st.set_page_config(
    page_title="Invoice Extractor App",
    layout="wide"
)

st.header('Invoice Extractor', divider='rainbow')
st.header('_Generative AI_ is :blue[cool] :sunglasses:')

prompt = st.text_input('What would you like to know?')

uploaded_file = st.file_uploader("Upload an image of the invoice...", type=["jpg", "jpeg", "png"])

image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')
    
submit = st.button('SUBMIT', type='primary')

system_prompt = '''

'''

if submit:
    with st.spinner("Generating response..."):
        response = generate_gemini_response(image,prompt) 
    st.success('Response generated successfully!', icon="✅")
    st.subheader("Here you go...")
    st.write(response)