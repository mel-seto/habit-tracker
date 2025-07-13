from datetime import date
from typing import Dict, Any


def add_habit(habit_name:str, data: Dict[str, Any]) -> None:
    if habit_name in data:
        raise ValueError(f"Habit '{habit_name}' already exists")
    data[habit_name] = {
        "streak": 0,
        "last_done": None
    }

def mark_done(habit_name:str, data: Dict[str, Any]) -> None:
    today = date.today().isoformat()
    habit = data.get(habit_name)

    if not habit:
        raise ValueError(f"Habit '{habit_name}' does not exist")

    if habit["last_done"] != today:
        habit["streak"] += 1
        habit["last_done"] = today
