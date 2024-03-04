import streamlit as st
import base64
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

personalinfo=[]
def creds_entered():
    if st.session_state["passwd1"].strip()== "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.header(" \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            st.header(" \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            st.warning("Пожалуйства введите пароль")
        elif not st.session_state["user"]:
            st.warning("Пожалуйства введите логин")
        else:

            st.error(" такого пароля быть не может :face_with_raised_eyebrow:")

st.header(" \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
st.header(" \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="придумайте пароль", value="", key="passwd1", type="password", on_change=creds_entered)
        st.text_input(label="повторите пароль", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="придумайте пароль", value="", key="passwd1", type="password", on_change=creds_entered)
            st.text_input(label="повторите пароль", value="", key="passwd", type="password", on_change=creds_entered)
            return False
if authenticate_user():
    st.write("you're in")





st.header("    \n                                           Регестрация")
st.date_input("ваш день рождения", key="bd")

email = st.text_input('Почта', '@gmail.com')
phonenum = st.text_input('номер телеофна', '+7')

if st.button("зарегестрироваться"):
    st.session_state.personalinfo
.element {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: lightgreen;}