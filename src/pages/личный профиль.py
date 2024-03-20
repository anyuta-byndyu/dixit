import streamlit as st
import base64
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import sqlite3
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
right: 5rem;7
}}


</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


with stylable_container(
    key="profilepic",
    css_styles="""
    div[data-testid="stImage"] > img {
        position: absolute;
        left: 50%; /* Центрирование изображения по горизонтали */
        transform: translateX(-50%); /* Сдвиг изображения влево на половину его ширины */
        border-radius: 50%; /* Круглое обрезание изображения */
        object-fit: cover;
        width: 170px;
        height: 170px;
    }
    """
):
    profilepic =st.image('./shark.jpg')

num_lines = 10
add_vertical_space(num_lines)

new_quizz=st.button(":green[создать новый квиз]")
if new_quizz == "создать новый квиз":
    switch_page("создание квиза")
st.divider()
data_df = pd.DataFrame(
    {
        "мои квизы": ["название 1", "название 2", "название 3"],
        "скачать результаты": ["результаты1","результаты2","результаты3"],
        "скачать квиз": ["квиз 1","квиз 2","квиз 3"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "мои квизы",
            help="список ваших квизов",
            width="medium",
            options=["результаты1","результаты2","результаты3"],
            required=True,
        )
    },
    hide_index=True,
)