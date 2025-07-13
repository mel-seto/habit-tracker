from habit_tracker.core import add_habit, mark_done, is_done_today
from datetime import date
from copy import deepcopy


def today_str(offset=0):
    return (date.today()).isoformat()


def test_add_new_habit():
    data = {}
    updated = add_habit("meditate", deepcopy(data))
    assert "meditate" in updated
    assert updated["meditate"]["dates"] == []


def test_add_existing_habit_is_idempotent():
    data = {"meditate": {"dates": []}}
    updated = add_habit("meditate", deepcopy(data))
    assert updated == data  # No change


def test_mark_done_adds_today():
    today = date.today().isoformat()
    data = {"meditate": {"dates": []}}

    updated = mark_done("meditate", deepcopy(data), today=today)

    assert today in updated["meditate"]["dates"]


def test_mark_done_does_not_duplicate_today():
    today = date.today().isoformat()
    data = {"meditate": {"dates": [today]}}

    updated = mark_done("meditate", deepcopy(data), today=today)

    assert updated["meditate"]["dates"].count(today) == 1


def test_mark_done_raises_if_habit_missing():
    data = {}
    try:
        mark_done("nonexistent", deepcopy(data))
    except ValueError as e:
        assert "does not exist" in str(e)
    else:
        assert False, "Expected ValueError"


def test_is_done_today_true():
    today = date.today().isoformat()
    data = {"meditate": {"dates": [today]}}

    assert is_done_today("meditate", data, today=today) is True


def test_is_done_today_false():
    today = date.today().isoformat()
    data = {"meditate": {"dates": []}}

    assert is_done_today("meditate", data, today=today) is False
