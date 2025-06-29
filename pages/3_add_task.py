import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from data import Task
import datetime
from utils.state_utils import init_session_state
from data import load_data_from_json, save_data_to_json

init_session_state()

st.write(st.session_state)

st.title("タスクを追加")

# テスト用データ
# if "goals" not in st.session_state:
#     st.session_state.goals = load_data_from_json("data/goals.json")
# if "current_goal" not in st.session_state:
#     st.session_state.current_goal = st.session_state.goals[0] # ほんとうは渡されてくる
current_subgoals = st.session_state.current_goal.subgoals

n_subgoals = len(current_subgoals)

if "task_counts" not in st.session_state:
    st.session_state.task_counts = [1] * n_subgoals

for subgoal_i, subgoal in enumerate(current_subgoals):
    st.subheader(subgoal.title)
    st.write(f"期限: {subgoal.due_date}")

    # タスクの追加フォーム
    # ここは表示を増やすだけ
    for i in range(st.session_state.task_counts[subgoal_i]):
        with st.container(border=True):
            task_title = st.text_input(
                f"タスク名 ",
                key=f"task_title_{subgoal_i}_{i}",
                placeholder="タスク名を入力してください"
                )
            task_due_date = st.date_input(
                f"期限",
                value=datetime.date.today(),
                key=f"task_due_date_{subgoal_i}_{i}"
                )

    if st.button(f"追加", key=f"btn_add_task_{subgoal_i}"):
        if task_title.strip() == "":
            st.warning("タスク名を入力してください。")
        else:
            st.session_state.task_counts[subgoal_i] += 1
            st.rerun()

    # with st.form(key=f"task_form_{i}"):
    #     task_title = st.text_input("タスク名", key=f"task_title_{i}", value="", placeholder="タスク名を入力してください")
    #     task_due_date = st.date_input("締切日", datetime.date.today(), key=f"task_due_date_{i}")

    #     if st.form_submit_button("タスクを追加"):
    #         new_task = Task(title=task_title, due_date=task_due_date, status="in_progress")
    #         subgoal.tasks.append(new_task)
    #         st.rerun()


            # new_task = Task(title=task_title, due_date=task_due_date, status="in_progress")
            # subgoal.tasks.append(new_task)
# 全部一気に確定
task_found = False
if st.button("完了"):
    for subgoal_i in range(n_subgoals):
        for task_i in range(st.session_state.task_counts[subgoal_i]):
            task_title = st.session_state.get(f"task_title_{subgoal_i}_{task_i}", "").strip()
            task_due_date = st.session_state.get(f"task_due_date_{subgoal_i}_{task_i}", datetime.date.today())
            if task_title:
                task_found = True
                new_task = Task(title=task_title, due_date=task_due_date, status="in_progress")
                current_subgoals[subgoal_i].tasks.append(new_task)
    if not task_found:
        st.warning("最低1つはタスクを入力してください。")
    else:
        st.session_state.goals.append(st.session_state.current_goal)
        save_data_to_json("data/goals.json", st.session_state.goals)
        del st.session_state.current_goal
        del st.session_state.task_counts
        del st.session_state.selected_subgoal_index
        del st.session_state.num_subgoals
        st.switch_page("app.py")
