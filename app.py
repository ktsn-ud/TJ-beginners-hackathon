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

html = """
<div style="overflow-y: auto; padding: 12px; border: 1px solid #ccc; border-radius: 12px;">
"""

for goal in goals:
    goal_block = f"""
    <div style="border: 2px solid #007ACC; padding: 12px; border-radius: 10px; margin-bottom: 20px; background-color: #f0f8ff;">
        <h2>{goal.title}</h2>
        <p><strong>期限:</strong> {goal.due_date.strftime('%Y-%m-%d')}</p>
    """
    for subgoal in goal.subgoals:
        goal_block += f"""
        <div style="margin-left: 20px; border: 1px solid #999; padding: 10px; margin-top: 10px; border-radius: 8px; background-color: #fafafa;">
            <h4>{subgoal.title}</h4>
            <p><strong>期限:</strong> {subgoal.due_date.strftime('%Y-%m-%d')}</p>
            <ul>
        """
        for task in subgoal.tasks:
            status_color = "#28a745" if task.status == "done" else "#ffc107"
            goal_block += f"<li><span style='color:{status_color}; font-weight:bold;'>[{task.status}]</span> {task.title}（{task.due_date.strftime('%Y-%m-%d')}）</li>"

        goal_block += "</ul></div>"

    goal_block += "</div>"
    html += goal_block

html += "</div>"

components.html(html, height=650, scrolling=True)