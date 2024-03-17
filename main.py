from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables
import streamlit as st
import os
import re
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap
## Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def clean_text(text):
  # Remove special characters and punctuation
  text = re.sub(r"[^\w\s]", " ", text)
  # Remove single characters
  text = re.sub(r"\b[a-zA-Z]\b", " ", text)
  # Remove HTML tags
  text = re.sub(r"<[^>]*>", " ", text)
  # Lowercase the text
  text = text.lower()
  # Remove extra whitespace
  text = re.sub(r"\s+", " ", text)
  # Trim leading and trailing spaces
  text = text.strip()
  return text

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro', generation_config = {
        "temperature": 0,
    })
    response=model.generate_content([prompt,question])
    return response.text
st.set_page_config(page_title="Sentiment analysis")
st.header("Sentiment Analysis on User feedback")

sentiment=st.text_input("Input user sentiment: " ,key="input")
sentiment = clean_text(sentiment)

submit=st.button("Analyse")
st.subheader("Output")

prompt = f"""
You are an expert linguist, who is good at classifying customer review sentiments into Positive/Negative labels.
Help me classify customer reviews into: Positive, and Negative class.
In your output, only return the String as output
"""

# if submit is clicked
if submit:
    response=get_gemini_response(sentiment,prompt)
    st.text(response)

