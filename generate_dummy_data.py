from habit_tracker.storage import save_data

dummy_data = {
    "meditate": {
        "logs": [
            {"timestamp": "2025-07-19T08:30:00", "focus_rating": 4, "notes": "Morning calm"},
            {"timestamp": "2025-07-18T08:00:00", "focus_rating": 3, "notes": "Distracted today"},
            {"timestamp": "2025-07-17T08:15:00", "focus_rating": 5, "notes": "Felt great"}
        ]
    },
    "study Chinese": {
        "logs": [
            {"timestamp": "2025-07-19T19:00:00", "focus_rating": 5, "notes": "Reviewed flashcards"},
            {"timestamp": "2025-07-18T20:00:00", "focus_rating": 4, "notes": "Practiced speaking"},
            {"timestamp": "2025-07-16T19:30:00", "focus_rating": 3, "notes": "Tired, but kept going"}
        ]
    },
    "exercise": {
        "logs": [
            {"timestamp": "2025-07-19T07:00:00", "focus_rating": 3, "notes": "Short walk"},
            {"timestamp": "2025-07-17T07:00:00", "focus_rating": 4, "notes": "Good energy"},
            {"timestamp": "2025-07-15T07:30:00", "focus_rating": 2, "notes": "Felt sluggish"}
        ]
    }
}

if __name__ == "__main__":
    save_data(dummy_data)
    print("Dummy habit data saved!")
