# 🧠 Habit Tracker (CLI)

A simple Python command-line app to help you build habits and track your daily progress.  
Stores your data in a local `habits.json` file.

---

## 🚀 Features

- ✅ Add habits
- 📅 Mark habits as done today
- 📋 List all habits and show whether they’re done for today

---

## 🛠️ Installation

1. **Clone the repo:**

    ```bash
    git clone https://github.com/your-username/habit-tracker.git
    cd habit-tracker
    ```

2. **Create a virtual environment:**

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## 🧪 Run tests

```bash
pytest
```

---

## 🧑‍💻 Usage

Run the CLI using Python's `-m` flag (thanks to `__main__.py`):

```bash
python -m habit_tracker add meditate
python -m habit_tracker done meditate
python -m habit_tracker list
```

---

## 📝 Example Output

### Add a habit

```bash
$ python -m habit_tracker add meditate
✅ Added habit: meditate
```

### Mark as done

```bash
$ python -m habit_tracker done meditate
📅 Marked 'meditate' as done for today
```

### List habits

```bash
$ python -m habit_tracker list
📋 Your habits:
  ✅ meditate
  ❌ read
```

---

## 🧠 How It Works

All habits are saved to a local file named `habits.json`.  
Each habit stores the dates you marked it done.

Example contents of `habits.json`:

```json
{
  "meditate": {
    "dates": ["2025-07-11"]
  },
  "read": {
    "dates": []
  }
}
```

---

## ✅ Requirements

- Python 3.12+
- Dependencies listed in `requirements.txt`

---

## 📂 Project Structure

```
habit-tracker/
├── habit_tracker/
│   ├── __init__.py
│   ├── __main__.py      # ← lets you use python -m habit_tracker
│   ├── cli.py           # command-line interface
│   ├── core.py          # core logic (pure functions)
│   ├── storage.py       # file I/O (load/save JSON)
├── tests/
│   ├── test_core.py
│   ├── test_cli.py
├── requirements.txt
├── README.md
├── habits.json          # auto-created on first use
```

---

## 🎓 License

MIT
