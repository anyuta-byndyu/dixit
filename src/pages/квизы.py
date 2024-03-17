import streamlit as st
import base64
import sqlite3
conn= sqlite3.connect("data.db", check_same_thread= False)
cur = conn.cursor()
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("plain.jpg")

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
cur.execute('SELECT * FROM addingquestions')
data = cur.fetchall()
conn.close()







