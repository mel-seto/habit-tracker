from datetime import date
from typing import Dict, Any, Optional


def add_habit(name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    if name not in data:
        data[name] = {"dates": []}
    return data


def mark_done(name: str, data: Dict[str, Any], today: Optional[str] = None) -> Dict[str, Any]:
    if name not in data:
        raise ValueError(f"Habit '{name}' does not exist.")

    today = today or date.today().isoformat()
    if today not in data[name]["dates"]:
        data[name]["dates"].append(today)
        data[name]["dates"].sort()
    return data


def is_done_today(name: str, data: Dict[str, Any], today: Optional[str] = None) -> bool:
    today = today or date.today().isoformat()
    return today in data.get(name, {}).get("dates", [])
