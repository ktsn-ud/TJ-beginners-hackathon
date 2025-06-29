import os
import streamlit as st
from data import Task, Subgoal, Goal, load_data_from_json, save_data_to_json

json_path = "data/goals.json"

if "goals" not in st.session_state:
    st.session_state.goals = load_data_from_json(json_path) if os.path.exists(json_path) else []
goals = st.session_state.goals

selected_goal_index = st.session_state.get("selected_goal", 0)
selected_goal = goals[selected_goal_index]

if st.button("🏠 ホームに戻る"):
    del st.session_state.selected_goal
    st.switch_page("app.py")

st.title(selected_goal.title)
st.text(f"期限: {selected_goal.due_date.strftime('%Y-%m-%d')}")

for subgoal in selected_goal.subgoals:
    with st.container(border=True):
        st.header(subgoal.title)
        st.write(f"期限: {subgoal.due_date}")
        tasks_in_progress = []
        tasks_completed = []
        if subgoal.tasks:
            for task in subgoal.tasks:
                if task.status == "in_progress":
                    tasks_in_progress.append(task)
                elif task.status == "done":
                    tasks_completed.append(task)

        st.subheader("進行中のタスク")
        if tasks_in_progress:
            for task in tasks_in_progress:
                st.write(f"- {task.title} (期限: {task.due_date})")
        else:
            st.write("進行中のタスクはありません。")

        st.subheader("完了したタスク")
        if tasks_completed:
            for task in tasks_completed:
                st.write(f"- {task.title} (期限: {task.due_date})")
        else:
            st.write("完了したタスクはありません。")
