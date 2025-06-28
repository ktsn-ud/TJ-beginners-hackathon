from dataclasses import dataclass
import datetime

@dataclass
class Task: # 小目標
    title: str
    due_date: datetime.date
    status: str

@dataclass
class Subgoal: # 中目標
    title: str
    due_date: datetime.date
    tasks: list[Task]

@dataclass
class Goal: # 大目標
    title: str
    due_date: datetime.date
    subgoals: list[Subgoal]




