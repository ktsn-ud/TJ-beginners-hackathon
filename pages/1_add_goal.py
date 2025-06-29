import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from data import Goal
import datetime
from utils.state_utils import init_session_state

init_session_state()
st.title("計画を作成")
title = st.text_input("計画のタイトル", placeholder="計画のタイトルを入力してください")
due_date = st.date_input("期限", datetime.date.today())

if st.button("次へ（中期目標の作成）"):
    if title.strip() == "":
        st.warning("計画のタイトルを入力してください。")
    else:
        st.session_state.current_goal = Goal(title=title, due_date=due_date, subgoals=[])
        st.switch_page("pages/2_add_subgoal.py")
