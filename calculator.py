import tkinter as tk


def button_click(value):
    current = display.get()

    if value == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "C":
        display.delete(0, tk.END)

    else:
        display.insert(tk.END, value)


window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")
window.resizable(False, False)
window.configure(bg="#222222")


display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bg="#333333",
    fg="white",
    insertbackground="white",
    borderwidth=0
)

display.pack(
    padx=15,
    pady=20,
    fill="x",
    ipady=10
)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]


for row in buttons:
    frame = tk.Frame(window, bg="#222222")
    frame.pack(fill="both", expand=True, padx=10)

    for value in row:
        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 18),
            command=lambda v=value: button_click(v),
            bg="#444444",
            fg="white",
            activebackground="#666666",
            activeforeground="white",
            borderwidth=0
        )

        button.pack(
            side="left",
            fill="both",
            expand=True,
            padx=3,
            pady=3
        )


window.mainloop()