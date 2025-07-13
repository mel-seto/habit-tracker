import json
import os
from pathlib import Path
from typing import Dict, Any

FILE_PATH = Path(os.environ.get("HABIT_TRACKER_PATH", "habits.json"))

def load_data() -> Dict[str, Any]:
    if FILE_PATH.exists():
        with FILE_PATH.open("r") as f:
            return json.load(f)
    return {}


def save_data(data: Dict[str, Any]) -> None:
    with FILE_PATH.open("w") as f:
        json.dump(data, f, indent=2)
