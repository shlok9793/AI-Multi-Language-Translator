import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page setup
st.set_page_config(page_title="Generative AI-powered Translator", layout="centered")

# App title and intro
st.title("🌍 Generative AI-powered Translator")
st.markdown("Translate text from one language to another using OpenAI's GPT model.")

# Input box
input_text = st.text_area("Enter text to translate:", height=150, placeholder="Example: Hello, how are you?")

# Language options
languages = ["English", "French", "Spanish", "German", "Hindi", "Chinese", "Arabic", "Japanese", "Russian"]
source_lang = st.selectbox("Translate From", languages, index=0)
target_lang = st.selectbox("Translate To", languages, index=1)

# Translate button
if st.button("Translate") and input_text.strip():
    if source_lang == target_lang:
        st.warning("Please select different source and target languages.")
    else:
        with st.spinner("Translating..."):
            prompt = f"Translate the following text from {source_lang} to {target_lang}. Preserve the context and tone:\n\n{input_text}"

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                translation = response['choices'][0]['message']['content']
                st.text_area("Translated Text:", translation, height=150)

                st.download_button(
                    label="📥 Download Translation",
                    data=translation,
                    file_name="translation.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
