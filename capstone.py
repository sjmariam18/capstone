import streamlit as st

# Page Title
st.title("My Streamlit Webpage")

# Subtitle
st.subheader("Welcome to my simple Streamlit App")

# Text content
st.write("This is a normal page created using Streamlit.")

# Header
st.header("Features")

# Bullet points
st.markdown("""
- Easy to use
- Interactive UI
- Python-based
""")

# Input text from user
name = st.text_input("Enter your name:")

# Button action
if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to the app 😊")

# Footer
st.write("---")
st.caption("Developed using Streamlit")
