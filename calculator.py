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
window.geometry("300x400")

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)
display.pack(
    padx=10,
    pady=20,
    fill="x"
)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True)

    for value in row:
        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 18),
            command=lambda v=value: button_click(v)
        )
        button.pack(
            side="left",
            fill="both",
            expand=True,
            padx=2,
            pady=2
        )

window.mainloop()