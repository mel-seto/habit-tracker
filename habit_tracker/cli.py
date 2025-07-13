# habit_tracker/cli.py

import argparse
import json
import os
from .core import add_habit, mark_done, list_habits

DATA_FILE = os.getenv("HABIT_TRACKER_DATA_PATH", "habits.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add <habit>
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("habit")

    # done <habit>
    done_parser = subparsers.add_parser("done", help="Mark habit as done")
    done_parser.add_argument("habit")

    # list
    subparsers.add_parser("list", help="List all habits")

    args = parser.parse_args()
    data = load_data()

    try:
        if args.command == "add":
            add_habit(args.habit, data)
            print(f"✅ Added habit: {args.habit}")
        elif args.command == "done":
            mark_done(args.habit, data)
            print(f"📅 Marked '{args.habit}' as done for today")
        elif args.command == "list":
            habits = list_habits(data)
            if habits:
                print("📋 Your habits:")
                for h in habits:
                    print(f"  - {h}")
            else:
                print("⚠️ No habits tracked yet.")
    except Exception as e:
        print(f"❌ Error: {e}")

    save_data(data)

if __name__ == "__main__":
    main()
