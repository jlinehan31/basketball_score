import streamlit as st

home_team = st.sidebar.text_input('Home Team')
away_team = st.sidebar.text_input('Away Team')
# game_length
# shot_clock
# reset_button = st.sidebar.button('RESET')

# Create columns for score output and click updates
col1, col2 = st.columns(2)
with col1:
    home_score = st.number_input(
        home_team.upper(),
        min_value=0,
        value=0
    )

with col2:
    away_score = st.number_input(
        away_team.upper(),
        min_value=0,
        value=0
    )

# Add balloon celebration
if home_score == 100:
    st.balloons()
elif away_score == 100:
    st.balloons()
