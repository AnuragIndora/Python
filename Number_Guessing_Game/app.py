import streamlit as st
import random

# Initialize or reset session state
if "seceret_number" not in st.session_state:
    st.session_state.seceret_number = random.randint(0, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False


st.title("Number Guessing Game")

st.write("I am a thinking of a number between 0 to 100. Can you guess it ?")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess", min_value = 0, max_value=100, step=1, key="guess_input")
    guess_button = st.button("Guess")

    if guess_button:
        st.session_state.attempts += 1
        if guess < st.session_state.seceret_number:
            st.warning("Too low! try again.")
        elif guess > st.session_state.seceret_number:
            st.warning("Too high! try again.")
        else:
            st.success(f"Congratulation! You guess the correct number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True


# Reser Button 
if st.button("Reset Game"):
    st.session_state.seceret_number = random.randint(0, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()
