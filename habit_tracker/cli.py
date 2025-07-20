import argparse
from datetime import date, datetime

from .core import add_habit, log_activity, is_done_today, get_logs_by_habit
from .storage import load_data, save_data


def cli_add(args):
    data = load_data()
    data = add_habit(args.name, data)
    save_data(data)
    print(f"✅ Added habit: {args.name}")

def cli_list(args):
    data = load_data()
    if not data:
        print("⚠️ No habits tracked yet.")
        return

    print("📋 Your habits:")
    for habit in sorted(data.keys()):
        done = is_done_today(habit, data)
        status = "✅" if done else "❌"
        print(f"  {status} {habit}")

def cli_log(args):
    data = load_data()
    if args.name not in data:
        print(f"⚠️ Habit '{args.name}' does not exist. Add it first with `add`.")
        return

    try:
        focus = int(input("Focus rating (1–5)? "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a number from 1 to 5.")
        return

    notes = input("Any notes? ")

    data = log_activity(args.name, data, focus=focus, notes=notes)
    save_data(data)
    print(f"📝 Logged activity for '{args.name}' with focus {focus}")

def print_logs_by_habit(logs_by_habit):
    if not any(logs_by_habit.values()):
        print("⚠️ No logs found.")
        return

    for habit, logs in logs_by_habit.items():
        if not logs:
            continue
        print(f"\n📖 Logs for '{habit}':")
        for entry in logs:
            dt = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d %H:%M")
            focus = entry.get("focus_rating", "?")
            notes = entry.get("notes", "")
            print(f"  - {dt} | Focus: {focus} | Notes: {notes}")


def cli_logbook(args):
    data = load_data()
    logs = get_logs_by_habit(data)  # no limit for full history
    print_logs_by_habit(logs)

def cli_recent(args):
    data = load_data()
    limit = args.limit
    logs = get_logs_by_habit(data, limit=limit)
    print_logs_by_habit(logs)

def main():
    parser = argparse.ArgumentParser(description="🧠 Simple Habit Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", help="Name of the habit")
    add_parser.set_defaults(func=cli_add)

    # list
    list_parser = subparsers.add_parser("list", help="List all habits and their done status")
    list_parser.set_defaults(func=cli_list)

    # log
    log_parser = subparsers.add_parser("log", help="Log focus + notes for a habit")
    log_parser.add_argument("name", help="Name of the habit")
    log_parser.set_defaults(func=cli_log)

    # logbook
    logbook_parser = subparsers.add_parser("logbook", help="Show all logs grouped by habit")
    logbook_parser.set_defaults(func=cli_logbook)

    # recent
    recent_parser = subparsers.add_parser("recent", help="Show recent logs per habit")
    recent_parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Number of recent logs to show per habit (default: 3)"
    )
    recent_parser.set_defaults(func=cli_recent)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
