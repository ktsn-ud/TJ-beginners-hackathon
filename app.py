import streamlit as st
import streamlit.components.v1 as components
from data import Task, Subgoal, Goal, load_data_from_json
from utils.state_utils import init_session_state

st.set_page_config(
    page_title="タスク管理アプリ",
    layout="centered"
)

# セッション変数の初期化
init_session_state()

# ここからトップページ #########

# -------------------
# データ読み込み
# -------------------
goals = load_data_from_json("test_data.json")
st.title("タスク管理アプリ")

# ページリンクを表示
st.markdown("### [📌 目標を追加](./1_add_goal)")

html = """
<div style="padding: 12px; border: 1px solid #ccc; border-radius: 12px;">
"""

for goal in goals:
    goal_block = f"""
    <div style="border: 2px solid #007ACC; padding: 12px; border-radius: 10px; margin-bottom: 20px; background-color: #f0f8ff;">
        <h2>{goal.title}</h2>
        <p><strong>期限:</strong> {goal.due_date.strftime('%Y-%m-%d')}</p>
    </div>
    """
    html += goal_block

html += "</div>"

components.html(html, height=goals.__len__() * 200, scrolling=False)