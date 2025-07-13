# tests/test_cli.py

import os
import json
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def run_cli(args, data_file):
    env = os.environ.copy()
    env["HABIT_TRACKER_PATH"] = str(data_file)

    result = subprocess.run(
        ["python", "-m", "habit_tracker.cli"] + args,
        env=env,
        capture_output=True,
        text=True,
        check=True
    )
    return result

def test_add_creates_habits_json(tmp_path):
    data_file = tmp_path / "habits.json"
    run_cli(["add", "meditate"], data_file)

    assert data_file.exists()
    data = json.loads(data_file.read_text())
    assert "meditate" in data


def test_list_outputs_habits(tmp_path):
    data_file = tmp_path / "habits.json"
    run_cli(["add", "read"], data_file)
    run_cli(["add", "stretch"], data_file)

    result = run_cli(["list"], data_file)
    assert "read" in result.stdout
    assert "stretch" in result.stdout
