import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from data import Task
import datetime
from utils.state_utils import init_session_state
from data import load_data_from_json, save_data_to_json

init_session_state()

st.title("タスクを追加")

st.write(st.session_state)

# テスト用データ
if "goals" not in st.session_state:
    st.session_state.goals = load_data_from_json("data/goals.json")
if "current_goal" not in st.session_state:
    st.session_state.current_goal = st.session_state.goals[0] # ほんとうは渡されてくる
current_subgoals = st.session_state.current_goal.subgoals

if "task_count" not in st.session_state:
    st.session_state.task_count = 0
def show_tasks(subgoal):
    st.subheader(subgoal.title)
    st.write(f"締切日: {subgoal.due_date}")

    if subgoal.tasks:
        for task in subgoal.tasks:
            if task.status == 'done':
                continue
            st.write(f"- {task.title} (締切: {task.due_date}, 状態: {task.status})")

for i, subgoal in enumerate(current_subgoals):
    if f"task_title_{i}" not in st.session_state:
        st.session_state[f"task_title_{i}"] = ""
    if f"task_due_date_{i}" not in st.session_state:
        st.session_state[f"task_due_date_{i}"] = datetime.date.today()

    show_tasks(subgoal)

    # タスクの追加フォーム
    with st.form(key=f"task_form_{i}"):
        task_title = st.text_input("タスク名", key=f"task_title_{i}", value="", placeholder="タスク名を入力してください")
        task_due_date = st.date_input("締切日", datetime.date.today(), key=f"task_due_date_{i}")

        if st.form_submit_button("タスクを追加"):
            new_task = Task(title=task_title, due_date=task_due_date, status="in_progress")
            subgoal.tasks.append(new_task)
            st.rerun()

if st.button("完了"):
    st.session_state.goals.append(st.session_state.current_goal)
    del st.session_state.current_goal
    st.switch_page("app.py")
