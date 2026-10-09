import json
from datetime import datetime
from pathlib import Path


HISTORY_FILE = Path(__file__).resolve().parent / "history.json"


def load_history():
    """Load previously saved calculations."""

    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            history = json.load(file)

        if isinstance(history, list):
            return history

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    """Save calculation history to a JSON file."""

    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def add_history(expression, result):
    """Add a calculation to history."""

    history = load_history()

    entry = {
        "expression": expression,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(entry)
    save_history(history)

    return entry


def show_history():
    """Display all saved calculations."""

    history = load_history()

    if not history:
        print("\nNo calculation history available.")
        return

    print("\n========== CALCULATION HISTORY ==========")

    for index, entry in enumerate(history, start=1):
        print(f"{index}. {entry['expression']} = {entry['result']}")
        print(f"   Time: {entry['timestamp']}")

    print("=========================================")


def clear_history():
    """Delete all saved calculations."""

    save_history([])
    print("\nCalculation history cleared.")


def delete_history_entry(index):
    """Delete one history entry using its 1-based index."""

    history = load_history()

    if index < 1 or index > len(history):
        raise IndexError("Invalid history entry number.")

    deleted_entry = history.pop(index - 1)
    save_history(history)

    return deleted_entry