import tkinter as tk
from operations import add, subtract, multiply, divide
from history import add_to_history, get_history, clear_history


# -----------------------------
# Calculator Logic
# -----------------------------

def button_click(value):
    current = display.get()

    if value == "=":
        try:
            if "+" in current:
                a, b = current.split("+")
                result = add(float(a), float(b))

            elif "-" in current:
                a, b = current.split("-")
                result = subtract(float(a), float(b))

            elif "*" in current:
                a, b = current.split("*")
                result = multiply(float(a), float(b))

            elif "/" in current:
                a, b = current.split("/")
                result = divide(float(a), float(b))

            else:
                result = float(current)

            if result == int(result):
                result = int(result)

            display.delete(0, tk.END)
            display.insert(0, str(result))

            # Add calculation to history
            add_to_history(current, result)
            update_history()

        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "C":
        display.delete(0, tk.END)

    else:
        display.insert(tk.END, value)


# -----------------------------
# History
# -----------------------------

def update_history():
    history_list.delete(0, tk.END)

    for calculation in get_history():
        history_list.insert(tk.END, calculation)


def clear_history_display():
    clear_history()
    history_list.delete(0, tk.END)


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()
window.title("Calculator")
window.geometry("720x560")
window.resizable(False, False)
window.configure(bg="#121212")


# -----------------------------
# Main Container
# -----------------------------

main_frame = tk.Frame(
    window,
    bg="#121212"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# =========================================================
# CALCULATOR
# =========================================================

calculator = tk.Frame(
    main_frame,
    bg="#1c1c1c",
    padx=18,
    pady=18
)

calculator.pack(
    side="left",
    fill="both",
    expand=True
)


# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    calculator,
    font=("Segoe UI", 32),
    justify="right",
    bg="#1c1c1c",
    fg="#f5f5f5",
    insertbackground="#f5f5f5",
    borderwidth=0
)

display.pack(
    fill="x",
    ipady=18,
    pady=(10, 25)
)


# -----------------------------
# Calculator Buttons
# -----------------------------

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]


for row in buttons:

    row_frame = tk.Frame(
        calculator,
        bg="#1c1c1c"
    )

    row_frame.pack(
        fill="both",
        expand=True
    )

    for value in row:

        if value == "=":
            bg_color = "#f5f5f5"
            fg_color = "#121212"
            active_bg = "#dcdcdc"

        elif value in ["C", "/", "*", "-", "+"]:
            bg_color = "#2a2a2a"
            fg_color = "#ffffff"
            active_bg = "#3a3a3a"

        else:
            bg_color = "#242424"
            fg_color = "#f5f5f5"
            active_bg = "#333333"

        button = tk.Button(
            row_frame,
            text=value,
            font=("Segoe UI", 17),
            bg=bg_color,
            fg=fg_color,
            activebackground=active_bg,
            activeforeground=fg_color,
            borderwidth=0,
            relief="flat",
            command=lambda v=value: button_click(v)
        )

        button.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )


# =========================================================
# HISTORY PANEL
# =========================================================

history_frame = tk.Frame(
    main_frame,
    bg="#1c1c1c",
    width=220,
    padx=15,
    pady=18
)

history_frame.pack(
    side="right",
    fill="y",
    padx=(15, 0)
)

history_frame.pack_propagate(False)


# -----------------------------
# History Title
# -----------------------------

history_title = tk.Label(
    history_frame,
    text="HISTORY",
    font=("Segoe UI", 12, "bold"),
    bg="#1c1c1c",
    fg="#f5f5f5"
)

history_title.pack(
    anchor="w",
    pady=(5, 15)
)


# -----------------------------
# History List
# -----------------------------

history_list = tk.Listbox(
    history_frame,
    font=("Segoe UI", 11),
    bg="#242424",
    fg="#dddddd",
    selectbackground="#3a3a3a",
    selectforeground="#ffffff",
    borderwidth=0,
    highlightthickness=0
)

history_list.pack(
    fill="both",
    expand=True
)


# -----------------------------
# Clear History Button
# -----------------------------

clear_button = tk.Button(
    history_frame,
    text="Clear History",
    font=("Segoe UI", 10),
    bg="#2a2a2a",
    fg="#ffffff",
    activebackground="#3a3a3a",
    activeforeground="#ffffff",
    borderwidth=0,
    relief="flat",
    command=clear_history_display
)

clear_button.pack(
    fill="x",
    pady=(15, 5),
    ipady=6
)


# -----------------------------
# Start Application
# -----------------------------

window.mainloop()