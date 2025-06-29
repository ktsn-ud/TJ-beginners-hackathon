import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from data import Goal
import datetime
from utils.state_utils import init_session_state

init_session_state()
st.title("大目標を作成")
title = st.text_input("大目標のタイトル")
due_date = st.date_input("大目標の期限", datetime.date.today())
if st.button("次へ(中期目標の追加)") and title:
    st.session_state.goal = Goal(title=title, due_date=due_date, subgoals=[])
    st.switch_page("pagea/2_add_subgoal.py")
