import streamlit as st
def join_game():
    st.title("Присоединиться к игре")

    code = st.number_input("Введите код игры (6 цифр)", min_value=100000, max_value=999999, step=1, format="%d")

    nickname = st.text_input("Введите ваш никнейм")

    if nickname.strip() == "":
        st.warning("Никнейм не может быть пустым!")
        return

    if st.button("Подтвердить"):
        st.success(f"Вы присоединились к игре с кодом {code} под никнеймом '{nickname}'.")


def main():
    join_game()

if __name__ == "__main__":
    main()



