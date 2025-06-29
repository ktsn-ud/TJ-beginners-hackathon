import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import datetime

from data import Goal, Subgoal, Task
from utils.state_utils import init_session_state

init_session_state()

# Goalが渡されているか確認
if "current_goal" not in st.session_state:
    st.error("先に計画を作成してください")
    st.stop()

# 大目標のタイトルを表示
st.title("中期目標の作成")

st.text(f"{st.session_state.current_goal.title}")
st.text(f"期限: {st.session_state.current_goal.due_date}")


# subgoalの数の初期化
if "num_subgoals" not in st.session_state:
    st.session_state.num_subgoals = 1

# サブゴールのタイトル、期限の入力欄
for i in range(st.session_state.num_subgoals):
    with st.container(border=True):
        title = st.text_input(f"中期目標{i + 1}のタイトル", key=f"subgoal_title_{i}", placeholder="中期目標のタイトルを入力してください")
        due_date = st.date_input(f"中期目標{i + 1}の期限", value=datetime.date.today(), key=f"subgoal_due_{i}")

# 追加ボタンクリック → サブゴール、期限の入力欄を増やす
if st.button("追加"):
    st.session_state.num_subgoals += 1
    st.rerun()

# 次へをクリック → サブゴールを追加 → Taskの入力ページへ
if st.button("次へ（タスクの作成）"):
    added_count = 0
    for i in range(st.session_state.num_subgoals):
        title = st.session_state.get(f"subgoal_title_{i}", "").strip()
        due_date = st.session_state.get(f"subgoal_due_{i}", datetime.date.today())
        if title:
            subgoal = Subgoal(title=title, due_date=due_date, tasks=[])
            st.session_state.current_goal.add_subgoal(subgoal)
            added_count += 1

    if added_count == 0:
        st.warning("最低1つは中期目標を入力してください。")
    else:
        st.session_state.selected_subgoal_index = 0
        st.switch_page("pages/3_add_task.py")