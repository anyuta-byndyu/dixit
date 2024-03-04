import base64
import streamlit as st
from streamlit_extras.stoggle import stoggle
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("qrcode.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stToolbar"] {{
right: 5rem;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
with st.sidebar:
    button = st.radio("присоединиться:", ["", "по qr-code", "по коду игры"])
    if button == "по qr-code":
        switch_page("присоединиться к игре по коду")
    if button == "по коду игры":
        switch_page("присоединиться к игре по qr-коду")


