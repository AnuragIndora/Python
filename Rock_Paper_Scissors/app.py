import streamlit as st
import random

# random and initiliaze 
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# game logic 
def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])


def determine_winner(user_choice, computer_choice, user):
    if user_choice == computer_choice:
        return "Game is Tie !"

    elif (user_choice == "rock" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "scissor") or \
        (user_choice == "scissor" and computer_choice == "rock"):
        st.session_state.computer_score += 1
        return "computer wins !"
    
    else:
        st.session_state.user_score += 1
        return f"{user} win !"

# UI
st.title("Rock-Paper-Scissor")
user_name = st.text_input("User Name : ", value="Player")

user_choice = st.radio("Choose your move:", ["rock", "paper", "scissor"])
if st.button("Play"):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice, user_name)

    st.write(f"User chose : {user_choice}")
    st.write(f"Computer chose : {computer_choice}")
    st.subheader(result)

    st.markdown("---")
    st.write("### Score ")
    st.write(f"{user_name} : {st.session_state.user_score}")
    st.write(f"Computer : {st.session_state.computer_score}")


# Reset Score 
if st.button("Reset Score"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Score have been reset.")