import streamlit as st
from pages.thank_you_page import display_thank_you

def display_thank_you():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Roboto:wght@300&display=swap');
    
    .background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .content {
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin-top:250px;
        width: 75%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    
    .large-text {
        font-family: 'Lobster', cursive;
        font-size: 100px;
        color: rgba(255, 255, 255, 0.8);
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        animation: colorChange 10s infinite;
        line-height: 1;
        margin-bottom: 5vh;
    }
    
    .small-text {
        font-family: 'Roboto', sans-serif;
        font-size: 3vw;
        color: white;
        margin-top: 1vh;
        animation: fadeInOut 5s infinite;
    }
    @keyframes colorChange {
        0% { color: rgba(255, 255, 255, 0.8); }
        33% { color: rgba(255, 223, 186, 0.8); }
        66% { color: rgba(186, 255, 201, 0.8); }
        100% { color: rgba(255, 255, 255, 0.8); }
    }
    @keyframes fadeInOut {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    </style>
    
    <div class="content">
        <div class="large-text">Thank You!</div>
        <div class="small-text">Thank you for visiting our site.</div>
        <div class="small-text">We hope you found what you were looking for.</div>
    </div>
    """, unsafe_allow_html=True)


