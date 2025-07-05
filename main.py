# import streamlit as st
# from datetime import datetime
# import openai
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# import pyttsx3

# # Load .env
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Gemini setup
# genai.configure(api_key=gemini_api_key)
# gemini_model = genai.GenerativeModel('gemini-2.5-flash')

# st.title("🛒 Grocery Reminder AI")

# items = st.text_area("Apni Grocery List Likhiye (comma se alag karein)", "doodh, sabzi, chawal")
# model_choice = st.radio("AI Model Choose Karein", ("OpenAI", "Gemini"))

# if st.button("AI Reminder Banao"):
#     prompt = f"Aik friendly Urdu reminder banao ke user ko yeh cheezein lene hain: {items}. Thoda pyar se bolo."

#     if model_choice == "OpenAI":
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "Aap ek Urdu grocery reminder bot hain."},
#                     {"role": "user", "content": prompt}
#                 ]
#             )
#             result = response['choices'][0]['message']['content']
#         except Exception as e:
#             result = f"❌ Error from OpenAI: {e}"

#     else:
#         try:
#             response = gemini_model.generate_content(prompt)
#             result = response.text
#         except Exception as e:
#             result = f"❌ Error from Gemini: {e}"

# # Text to Speech function
# def speak(text):
#     try:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print("TTS Error:", e)             

#     st.success("📢 Reminder:")
#     st.write(result)
#     st.success("📢 Reminder:")
#     speak(result)



import streamlit as st
from datetime import datetime
import openai
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pyttsx3

# Load .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini setup
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")  # ✅ recommended model name

# Text to Speech function
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

# UI
st.title("🛒 Grocery Reminder AI")

items = st.text_area("Write a grocery list (separate items with commas)", "doodh, sabzi, chawal")
model_choice = st.radio("Choose AI Model", ("OpenAI", "Gemini"))

if st.button("Create Reminder"):
    prompt = f"Aik friendly english reminder banao ke user ko yeh cheezein lene hain: {items}. Thoda pyar se bolo."

    if model_choice == "OpenAI":
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Aap ek Urdu grocery reminder bot hain."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response['choices'][0]['message']['content']
        except Exception as e:
            result = f"❌ Error from OpenAI: {e}"
    else:
        try:
            response = gemini_model.generate_content(prompt)
            result = response.text
        except Exception as e:
            result = f"❌ Error from Gemini: {e}"

    # ✅ Show and speak the result
    st.success("📢 Reminder:")
    st.write(result)
    speak(result)

