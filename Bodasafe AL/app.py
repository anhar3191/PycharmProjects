import streamlit as st
import google.generativeai as genai

# Replace with your Google AI Studio API key
API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemma-3-27b-it")

st.set_page_config(page_title="BodaSafe AI", page_icon="🏍️")

st.title("🏍️ BodaSafe AI")
st.write("AI-powered safety assistant for boda boda trips.")

start = st.text_input("📍 Starting Location")
destination = st.text_input("🎯 Destination")
details = st.text_area("Additional Information (Optional)")

if st.button("Analyze Trip"):
    if start and destination:

        prompt = f"""
You are a road safety assistant in Kampala, Uganda.

Starting location: {start}
Destination: {destination}
Extra details: {details}

Provide:
1. Possible safety risks.
2. Safety tips.
3. Advice for passengers.
4. Advice for riders.
5. Emergency recommendations if something goes wrong.

Keep the response clear and practical.
"""

        with st.spinner("Analyzing..."):
            response = model.generate_content(prompt)

        st.success("Analysis Complete")
        st.write(response.text)

    else:
        st.warning("Please enter both the starting location and destination.")