import datetime
import streamlit as st
from data import Task, Subgoal, Goal, load_data_from_json
from utils.state_utils import init_session_state
import os

st.set_page_config(
    page_title="タスク管理アプリ",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def go_to_add():
    st.switch_page("pages/1_add_goal.py")

# セッション変数の初期化
init_session_state()

# -------------------
# データ読み込み
# -------------------
json_path = "data/goals.json"

if "goals" not in st.session_state:
    st.session_state.goals = load_data_from_json(json_path) if os.path.exists(json_path) else []
goals = st.session_state.goals

st.title("タスク管理アプリ")

# ページリンク
if st.button("📌 計画を作成"):
        go_to_add()
# -------------------
# Goal 一覧表示
# -------------------
if goals:
    for gi, goal in enumerate(goals):
        with st.container():
            # ✅ Streamlit ウィジェットで正しく表示
            left_days = (goal.due_date - datetime.date.today()).days
            st.subheader(f"◎ {goal.title}")
            st.text(f"期限: {goal.due_date.strftime('%Y-%m-%d')} (あと {left_days} 日)")

            # ✅ ボタンで当たり判定 → セッションに保存 & ページ遷移
            if st.button("👉 詳細を見る", key=f"goal_btn_{gi}"):
                st.session_state.selected_goal = gi
                st.switch_page("pages/details.py")
else:
    st.write("計画はまだ作成されていません。")
    st.write("「計画を作成」ボタンから始めましょう！")
