history = []


def add_to_history(expression, result):
    history.append(f"{expression} = {result}")


def get_history():
    return history


def clear_history():
    history.clear()