import streamlit as st
import requests
import json
import pyperclip

st.title("Text Correction API")

paragraph = st.text_area("Enter text to correct:")

if st.button("Correct Text"):
    if paragraph:
        url = "https://7kscf4ely3.execute-api.ap-south-1.amazonaws.com/DeltaStage1/Deltaresource"
        payload = {"paragraph": paragraph}

        response = requests.post(url, json=payload)
        result = response.json()

        if response.status_code == 200:
            body = json.loads(result['body'])
            corrected_text = body['corrected_text']
            st.success("✅ Text Corrected")
            st.text_area("Corrected Text:", value=corrected_text, disabled=True)

            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(corrected_text)
                st.success("Copied!")
        else:
            st.error("Error: Unable to correct text")
    else:
        st.warning("Please enter some text")