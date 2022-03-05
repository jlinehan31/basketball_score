import pandas as pd
import streamlit as st
import plotly.express as px

home_team = st.sidebar.text_input(
    'Home Team',
    value='Home Team'
)

away_team = st.sidebar.text_input(
    'Away Team',
    value='Away Team'
)

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
if home_score % 50 == 0 and home_score != 0:
    st.balloons()
elif away_score % 50 == 0 and away_score != 0:
    st.balloons()

score_df = pd.DataFrame(
    {
        home_team: [home_score],
        away_team: [away_score]
    }
)

score_df = score_df.melt()


fig = px.bar(
    data_frame=score_df,
    x='variable',
    y='value',
    color='variable',
    labels={
        'variable': '',
        'value': ''
    }
)

fig.update(layout_showlegend=False)

st.plotly_chart(fig)
