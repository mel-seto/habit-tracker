import argparse
from datetime import date

from .core import add_habit, log_activity, is_done_today
from .storage import load_data, save_data


def cli_add(args):
    data = load_data()
    data = add_habit(args.name, data)
    save_data(data)
    print(f"✅ Added habit: {args.name}")


def cli_done(args):
    data = load_data()
    try:
        data = log_activity(args.name, data, current_time=date.today().isoformat())
        save_data(data)
        print(f"📅 Marked '{args.name}' as done for today")
    except ValueError as e:
        print(f"⚠️ {e}")


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


def main():
    parser = argparse.ArgumentParser(description="🧠 Simple Habit Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", help="Name of the habit")
    add_parser.set_defaults(func=cli_add)

    # done
    done_parser = subparsers.add_parser("done", help="Mark a habit as done today")
    done_parser.add_argument("name", help="Name of the habit")
    done_parser.set_defaults(func=cli_done)

    # list
    list_parser = subparsers.add_parser("list", help="List all habits and their done status")
    list_parser.set_defaults(func=cli_list)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
