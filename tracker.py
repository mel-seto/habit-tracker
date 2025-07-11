from data_manager import load_data, save_data


def add_habit(habit_name):
    data = load_data()
    if habit_name not in data:
        data[habit_name] = []
        save_data(data)
        print(f"✅ Added habit: {habit_name}")
    else:
        print(f"⚠️ Habit already exists.")