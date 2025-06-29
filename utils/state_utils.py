import streamlit as st
from data import load_data_from_json
import os

DATA_PATH = "data/goals.json"

def init_session_state():
    """セッション変数の初期化（初回のみ）"""
    if "goals" not in st.session_state:
        if os.path.exists(DATA_PATH):
            st.session_state.goals = load_data_from_json(DATA_PATH)
        else:
            st.session_state.goals = []
