import streamlit as st
from pages import thank_you_page

def display_chat_page():
    #st.set_page_config(page_title="Chat To Know About The Vendors Of Bags", page_icon=":pouch:")
    st.header("Chat to know about vendors :handbag:")

    # Add thank you icon to lower right corner
    st.markdown(
        """
        <style>
        .thank-you-icon {

            right:70px;
            bottom:50px;
            font-size: 24px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("End Chat"):
        st.switch_page(r"D:\SAP\pages\thank_you_page.py")

    user_query = st.text_input("Ask questions to get to know about the best vendor", key="chat_user_query")
    answer_text = st.empty()

    st.markdown(f"""
        <style>
        .main {{
            background-image: url("https://static.vecteezy.com/system/resources/previews/010/803/399/non_2x/background-with-colorful-shopping-bags-illustration-sale-and-discount-concept-vector.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .stHeader > h2 {{color: black !important;}}
        .stTextInput > label {{color: black !important;}}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("https://images.pexels.com/photos/2905238/pexels-photo-2905238.jpeg");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)

    options = ["👜 Handbags", "🧳 Travel Bags", "💼 Sleeve", "👜 Tote bag", "🎒 Trekking bags", "💻 Laptop bags"]
    st.sidebar.selectbox("What kind of bags would you like to search?", options, key="chat_bag_select")


