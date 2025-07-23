from habit_tracker.core import add_habit, log_activity, is_done_today, get_logs_by_habit
from datetime import datetime, date
from copy import deepcopy

def test_add_new_habit():
    data = {}
    updated = add_habit("meditate", deepcopy(data))
    assert "meditate" in updated
    assert updated["meditate"]["logs"] == []

def test_add_existing_habit_is_idempotent():
    data = {"meditate": {"logs": []}}
    updated = add_habit("meditate", deepcopy(data))
    assert updated == data  # No change

def test_log_activity_adds_entry():
    now = datetime.now().isoformat()
    data = {"meditate": {"logs": []}}

    updated = log_activity("meditate", deepcopy(data), focus_rating=3, notes="Decent session", current_time=now)

    assert len(updated["meditate"]["logs"]) == 1
    entry = updated["meditate"]["logs"][0]
    assert entry["timestamp"] == now
    assert entry["focus_rating"] == 3
    assert entry["notes"] == "Decent session"

def test_log_activity_raises_if_habit_missing():
    data = {}
    try:
        log_activity("nonexistent", deepcopy(data), focus_rating=2)
    except ValueError as e:
        assert "does not exist" in str(e)
    else:
        assert False, "Expected ValueError"

def test_is_done_today_true():
    today = date.today().isoformat()
    log_time = f"{today}T08:00:00"
    data = {"meditate": {"logs": [{"timestamp": log_time, "focus_rating": 4, "notes": ""}]}}

    assert is_done_today("meditate", data, today) is True

def test_is_done_today_false():
    today = date.today().isoformat()
    data = {"meditate": {"logs": []}}

    assert is_done_today("meditate", data, today) is False

def test_get_logs_by_habit_full_and_limited():
    data = {
        "meditate": {
            "logs": [
                {"timestamp": "2025-07-15T08:00:00"},
                {"timestamp": "2025-07-16T08:00:00"},
                {"timestamp": "2025-07-17T08:00:00"},
                {"timestamp": "2025-07-18T08:00:00"},
                {"timestamp": "2025-07-19T08:00:00"}
            ]
        }
    }

    # Full logbook (no limit)
    full_logs = get_logs_by_habit(data)
    assert len(full_logs["meditate"]) == 5
    assert full_logs["meditate"][0]["timestamp"] == "2025-07-19T08:00:00"

    # Limited to most recent 3
    recent_logs = get_logs_by_habit(data, limit=3)
    assert len(recent_logs["meditate"]) == 3
    assert recent_logs["meditate"][0]["timestamp"] == "2025-07-19T08:00:00"
    assert recent_logs["meditate"][-1]["timestamp"] == "2025-07-17T08:00:00"


def test_log_activity_does_not_duplicate():
    now = datetime.now().isoformat()
    data = {"meditate": {"logs": [{"timestamp": now}]}}

    updated = log_activity("meditate", deepcopy(data), current_time=now)

    assert len(updated["meditate"]["logs"]) == 1  # Still just one log