import streamlit as st
from utils.state_utils import init_session_state

st.set_page_config(
    page_title="タスク管理アプリ",
    layout="centered"
)

# セッション変数の初期化
init_session_state()

# ここからトップページ #########