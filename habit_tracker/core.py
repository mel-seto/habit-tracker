from datetime import datetime, date
from typing import Dict, Any, Optional, List


def add_habit(name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    if name not in data:
        data[name] = {"logs": []}
    return data


def log_activity(name: str, data: Dict[str, Any], current_time: Optional[str] = None, focus: Optional[int] = None, notes: Optional[str] = "") -> Dict[str, Any]:
    if name not in data:
        raise ValueError(f"Habit '{name}' does not exist.")

    entry = {
        "timestamp": current_time or datetime.now().isoformat(),
        "focus_rating": focus,
        "notes": notes
    }
    data[name]["logs"].append(entry)
    return data


def is_done_today(name: str, data: Dict[str, Any], current_time: Optional[str] = None) -> bool:
    current_time = current_time or date.today().isoformat()
    logs = data.get(name, {}).get("logs", [])
    return any(log["timestamp"].startswith(current_time) for log in logs)


def get_logs_by_habit(data: Dict[str, Any], limit: Optional[int] = None) -> Dict[str, List[Dict[str, Any]]]:
    logs_by_habit = {}

    for habit, info in data.items():
        logs = info.get("logs", [])
        sorted_logs = sorted(logs, key=lambda x: x["timestamp"], reverse=True)
        logs_by_habit[habit] = sorted_logs[:limit] if limit is not None else sorted_logs

    return logs_by_habit