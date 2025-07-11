import os
from tracker import add_habit
from data_manager import load_data, save_data

def setup_function():
    if os.path.exists("habits.json"):
        os.remove("habits.json")
    save_data({})

def teardown_function():
    if os.path.exists("habits.json"):
        os.remove("habits.json")

def test_add_habit_creates_new_entry():
    add_habit("Read")
    data = load_data()
    assert "Read" in data
    assert data["Read"] == []
