# 🧘 Habit Tracker (Command-Line)

A minimal command-line tool to track daily habits.  
Built in Python from scratch using TDD and `argparse`.

## ✨ Features

- ✅ Add a habit to track  
- ✅ Mark a habit as done for today  
- ✅ List all tracked habits  
- ✅ Persistent storage via `habits.json`  
- ✅ Written with unit tests (core + CLI)  
- ✅ Runs via `python -m habit_tracker`

## 🚀 Usage

**Add a new habit**

    $ python -m habit_tracker add meditate
    ✅ Added habit: meditate

**Mark it done for today**

    $ python -m habit_tracker done meditate
    📅 Marked 'meditate' as done for today

**List all habits**

    $ python -m habit_tracker list
    📋 Your habits:
      - meditate

**If no habits are tracked**

    $ python -m habit_tracker list
    ⚠️ No habits tracked yet.

**If you try to mark an unknown habit**

    $ python -m habit_tracker done unknown
    ❌ Error: Habit 'unknown' not found.

## 🧪 Installation

You'll need:

- Python 3.12+
- `pip`
- `pytest`

Set up your environment:

    git clone https://github.com/yourusername/habit-tracker.git
    cd habit-tracker
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## 🧪 Running Tests

Run all tests with:

    pytest

Includes tests for:

- Core logic (`add_habit`, `mark_done`, `list_habits`)
- CLI behavior (via subprocess and isolated test files)

## 📁 Project Structure

    habit-tracker/
    ├── habit_tracker/
    │   ├── __init__.py
    │   ├── core.py         # Core habit logic
    │   ├── cli.py          # CLI interface using argparse
    │   └── __main__.py     # Enables `python -m habit_tracker`
    ├── tests/
    │   ├── __init__.py
    │   ├── test_core.py
    │   └── test_cli.py
    ├── habits.json         # (generated at runtime)
    ├── requirements.txt
    └── README.md

## 💡 Why This Project?

This project was written from scratch as part of my Recurse Center application.  
It reflects how I approach code design, testing, and command-line UX.

## ✅ License

MIT — do what you want.
