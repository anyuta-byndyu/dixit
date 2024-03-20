import base64
import streamlit as st
import sqlite3
conn= sqlite3.connect("data.db", check_same_thread= False)
cur = conn.cursor()
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("justback.jpg")

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
if 'qa' not in st.session_state:
    st.session_state.qa = 1
add=st.button("новый вопрос")
minus = st.button("убрать вопрос")
if add:
    def qa():
        with st.form(key="qas"):
            quesitself = st.text_input("вопрос: ")
            answer1 = st.text_input("первый вариант ответа: ")
            answer2 = st.text_input("второй вариант ответа: ")
            answer3 = st.text_input("третий вариант ответа: ")
            answer4 = st.text_input("четвёртый вариант ответа: ")
            adding = st.form_submit_button(label="добавить вопрос")
            if adding == True:
                add_qustion(quesitself, answer1, answer2, answer3, answer4)


    def add_qustion(a, b, c, d, e):
        cur.execute(
            """CREATE TABLE IF NOT EXISTS addingquestions
                                    (QUESITSELF TEXT(50), ANSWER1 TEXT(50), ANSWER2 TEXT(50), ANSWER3 TEXT(50), ANSWER4 TEXT(50));""")
        cur.execute("INSERT INTO addingquestions VALUES (?,?,?,?,?)", (a, b, c, d, e))
        conn.commit()
        cur.close()
        conn.close()

        st.success("вопрос добавлен")


    qa()
    st.session_state.qa += 1
if minus:
    st.session_state.qa -= 1
    st.experimental_rerun()



cur= conn.cursor()
cur.execute("SELECT * FROM addingquestions ")
thedata = cur.fetchall()
st.write('thedata')
conn.commit()
cur.close()
conn.close()
