from habit_tracker.core import add_habit, log_activity, is_done_today
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

    updated = log_activity("meditate", deepcopy(data), focus=3, notes="Decent session", current_time=now)

    assert len(updated["meditate"]["logs"]) == 1
    entry = updated["meditate"]["logs"][0]
    assert entry["timestamp"] == now
    assert entry["focus_rating"] == 3
    assert entry["notes"] == "Decent session"

def test_log_activity_raises_if_habit_missing():
    data = {}
    try:
        log_activity("nonexistent", deepcopy(data), focus=2)
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
