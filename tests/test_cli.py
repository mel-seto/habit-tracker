# tests/test_cli.py

import os
import json
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def run_cli(args, data_file):
    env = os.environ.copy()
    env["HABIT_TRACKER_DATA_PATH"] = str(data_file)

    return subprocess.run(
        ["python", "-m", "habit_tracker.cli", *args],
        cwd=PROJECT_ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=True
    )

def test_add_creates_habits_json(tmp_path):
    data_file = tmp_path / "habits.json"
    run_cli(["add", "meditate"], data_file)

    assert data_file.exists()
    data = json.loads(data_file.read_text())
    assert "meditate" in data

def test_done_updates_streak(tmp_path):
    data_file = tmp_path / "habits.json"
    run_cli(["add", "exercise"], data_file)
    run_cli(["done", "exercise"], data_file)

    data = json.loads(data_file.read_text())
    assert data["exercise"]["streak"] == 1

def test_list_outputs_habits(tmp_path):
    data_file = tmp_path / "habits.json"
    run_cli(["add", "read"], data_file)
    run_cli(["add", "stretch"], data_file)

    result = run_cli(["list"], data_file)
    assert "read" in result.stdout
    assert "stretch" in result.stdout
