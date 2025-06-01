import streamlit as st
import random

# Dice ASCII Art
DICE_ART = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘",
    ),
}

# Initialize roll history
if "roll_history" not in st.session_state:
    st.session_state.roll_history = []

# UI
st.title("🎲 Dice Roll Simulator with History")
st.write("Click the button below to roll the die.")

if st.button("Roll Dice"):
    roll = random.randint(1, 6)
    st.session_state.roll_history.append(roll)  # Save roll to history
    st.subheader(f"You rolled a {roll}!")
    st.text("\n".join(DICE_ART[roll]))

# Roll History
if st.session_state.roll_history:
    st.markdown("---")
    st.write("### 📜 Roll History")
    st.write(", ".join(str(r) for r in st.session_state.roll_history))

# Reset history
if st.button("Reset History"):
    st.session_state.roll_history.clear()
    st.success("Roll history cleared!")
