# Habit Tracker

A simple command-line habit tracker built in Python.

---

## Features

- Add new habits  
- Mark habits as done for today  
- List all habits with completion status  
- View recent logs per habit with customizable limit  
- View full logbook of all habits  

---

## Installation

1. Clone the repository:

~~~bash
git clone https://github.com/yourusername/habit-tracker.git
cd habit-tracker
~~~

2. Create and activate a virtual environment:

~~~bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
~~~

3. Install dependencies:

~~~bash
pip install -r requirements.txt
~~~

---

## Usage

Run commands using:

~~~bash
python -m habit_tracker <command> [options]
~~~

---

### Commands

#### Add a new habit

~~~bash
python -m habit_tracker add "habit name"
~~~

Example:

~~~bash
python -m habit_tracker add meditate
~~~

---

#### Mark a habit as done today

~~~bash
python -m habit_tracker done "habit name"
~~~

Example:

~~~bash
python -m habit_tracker done meditate
~~~

---

#### List all habits and their status for today

~~~bash
python -m habit_tracker list
~~~

---

#### Show recent logs per habit

By default, shows the last 3 logs for each habit:

~~~bash
python -m habit_tracker recent
~~~

To customize how many recent logs to show, use the `--limit` option:

~~~bash
python -m habit_tracker recent --limit 5
~~~

---

#### Show full logbook (all logs per habit)

~~~bash
python -m habit_tracker logbook
~~~

---

## Testing

Run the test suite using:

~~~bash
pytest
~~~

---

## Development

- Core logic lives in `habit_tracker/core.py`  
- CLI commands in `habit_tracker/cli.py`  
- Data stored in a JSON file (default: `habits.json`)  

---

## License

[MIT License](LICENSE)
