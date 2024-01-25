import pandas as pd
import streamlit as st
from PIL import Image


def bullet_list(items):
    bullet_points = "\n".join([f"###  -   {item}" for item in items])
    st.markdown(bullet_points)


def resize_image(image, size):
    resized_image = image.resize(size)
    return resized_image


st.set_page_config(layout="wide")

col1, col2 = st.columns([2.2, 6])

with col1:
    st.write("")
    st.write("")
    st.write("")
    st.image(resize_image(Image.open("Abdallah Hossam-Eldin Photo.jpg"), (375, 500)))


with col2:
    st.title("Abdallah Hossam-Eldin Hosni")
    bullet_list(
        [
            "A fresh Electronic and Communication Engineering Graduate",
            "Vector Certified Embedded Associate",
        ],
    )

    content1 = """I am a recent graduate with a degree in Electronic and 
    Communication Engineering from Cairo University, and I have a passion 
    for developing embedded systems solutions for the automotive industry."""
    content2 = """I have a solid proficiency in programming languages such as C and C++, 
    particularly in the context of MCU programming. I have good experience 
    with micro-controller interfacing such as AVR and ARM-based micro-controllers 
    and their peripherals, with a good knowledge of UART, SPI, I2C, LIN, and CAN. 
    I also have very good knowledge of Python, which I can use for scripting 
    and data analysis."""
    content3 = """I have gained valuable experience with 
    AUTOSAR during my graduation project and my journey to become a Vector 
    Certified Embedded Associate. This experience involved using Vector 
    Informatik tools like DaVinci Developer, DaVinci Configurator Pro, and CANoe. 
    In my graduation project, **I developed an AUTOSAR-based automotive** inverter."""

    st.info(content1)
    st.info(content2)
    st.info(content3)


st.header("Hello Omar Ezz Sika, This is my website")

df = pd.read_csv("data.csv", sep=";")

col3, emptyCol, col4 = st.columns([8, 3, 8])

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Link to The Github Repository", row["url"])
        st.write(f"Or press the Link Directly: {row["url"]}")

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Link to The Github Repository", row["url"])
        st.write(f"Or press the Link Directly: {row["url"]}")
