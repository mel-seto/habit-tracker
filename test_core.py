from datetime import date

import pytest

import core


def test_add_habit_create_new_entry():
    data = {}
    core.add_habit("Read", data)
    assert "Read" in data


def test_add_habit_raises_if_exists():
    data = {"read": {"streak": 3, "last_done": "2024-07-10"}}


    with pytest.raises(ValueError):
        core.add_habit("read", data)


def test_mark_done_increments_streak_and_sets_today():
    data = {
        "read": {
            "streak": 2,
            "last_done": "2024-07-10"
        }
    }
    core.mark_done("read", data)

    assert data["read"]["streak"] == 3
    assert data["read"]["last_done"] == date.today().isoformat()


def test_mark_done_raises_if_habit_missing():
    data = {}

    with pytest.raises(ValueError):
        core.mark_done("meditate", data)


def test_mark_done_does_not_increase_streak_twice_in_a_day():
    today = date.today().isoformat()
    data = {
        "run": {
            "streak": 5,
            "last_done": today
        }
    }

    core.mark_done("run", data)

    assert data["run"]["streak"] == 5
    assert data["run"]["last_done"] == today
