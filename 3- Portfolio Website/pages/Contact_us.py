import streamlit as st

from send_email import sendMail

st.header("Contact Me")

with st.form(key="Contact Me Form"):
    userMail = st.text_input("Please, Enter your email address")
    message = st.text_area("Please, Enter your message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        with st.spinner("Wait for it..."):
            sendMail(message, userMail)
            st.success("Your message has been sent successfully")
