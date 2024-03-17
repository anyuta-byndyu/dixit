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


img = get_img_as_base64("long.jpg")

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




def regestration():
    with st.form(key="user_id"):
        name = st.text_input("важе имя: ")
        surname = st.text_input("важа фамилия: ")
        age = st.date_input("ваш день рождения", key="bd")
        email = st.text_input('Почта', '@gmail.com')
        phonenum = st.text_input('номер телеофна', '+7')
        password = st.text_input("придумайте пароль: ")
        repeatpassowrd = st.text_input(label="повторите пароль", value="", key="passwd1", type="password")
        submission = st.form_submit_button(label="зарегестрироваться")
        if submission == True:
            add_user(name, surname, age, email, phonenum, password )
def add_user(a,b,c,d,e,f):
    cur.execute("""CREATE TABLE IF NOT EXISTS regestrationuser(NAME TEXT(50), SURNAME TEXT(50), AGE TEXT(50), EMAIL TEXT(50), PHONENUM TEXT(50), PASSWORD TEXT(50));""")
    cur.execute("INSERT INTO regestrationuser VALUES (?,?,?,?,?,?)",(a,b,c,d,e,f))
    conn.commit()
    conn.close()
    st.success("вы успешно зарегестрировались")
regestration()