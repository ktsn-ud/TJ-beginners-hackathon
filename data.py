import json
import datetime
from dataclasses import dataclass, asdict
from typing import Literal


@dataclass
class Task:  # 小目標
    title: str
    due_date: datetime.date
    status: Literal["in_progress", "done"]


@dataclass
class Subgoal:  # 中目標
    title: str
    due_date: datetime.date
    tasks: list[Task]

    def add_task(self, task: Task):
        self.tasks.append(task)


@dataclass
class Goal:  # 大目標
    title: str
    due_date: datetime.date
    subgoals: list[Subgoal]

    def add_subgoal(self, subgoal: Subgoal):
        self.subgoals.append(subgoal)


def save_data_to_json(file_path: str, goals: list[Goal]):
    """データをJSONファイルに保存する"""

    def convert_dates(obj):
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        return obj

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([asdict(goal) for goal in goals], f, ensure_ascii=False, indent=4, default=convert_dates)


def load_data_from_json(file_path: str) -> list[Goal]:
    """JSONファイルからデータを読み込み、インスタンス化"""

    def parse_dates(obj):
        if "due_date" in obj:
            obj["due_date"] = datetime.datetime.strptime(obj["due_date"], "%Y-%m-%d").date()
        return obj

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f, object_hook=parse_dates)
        goals = []
        for g in data:
            subgoals = []
            for sg in g["subgoals"]:
                tasks = [Task(**t) for t in sg["tasks"]]
                subgoals.append(Subgoal(title=sg["title"], due_date=sg["due_date"], tasks=tasks))
            goals.append(Goal(title=g["title"], due_date=g["due_date"], subgoals=subgoals))
        return goals


# 以下テスト
if __name__ == "__main__":
    # テスト用のダミーデータを作成
    dummy_data = [
        Goal(
            title="英検合格",
            due_date=datetime.date(2024, 3, 31),
            subgoals=[
                Subgoal(
                    title="過去問を解く",
                    due_date=datetime.date(2024, 2, 29),
                    tasks=[
                        Task(
                            title="2023年度第1回",
                            due_date=datetime.date(2024, 1, 15),
                            status="done"
                        ),
                        Task(
                            title="2023年度第2回",
                            due_date=datetime.date(2024, 2, 1),
                            status="in_progress"
                        ),
                    ]
                ),
                Subgoal(
                    title="単語帳を覚える",
                    due_date=datetime.date(2024, 3, 1),
                    tasks=[
                        Task(
                            title="1000語覚える",
                            due_date=datetime.date(2024, 2, 15),
                            status="in_progress"
                        ),
                    ]
                ),
            ]
        )
    ]

    # 保存テスト
    save_data_to_json("test_data.json", dummy_data)

    # 読み込みテスト
    loaded_data = load_data_from_json("test_data.json")
    print(loaded_data)
