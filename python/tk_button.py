import tkinter as tk

root = tk.Tk()

root.geometry("640x480")
root.title("Buttons")


def on_click():
    print("Button clicked")


btn = tk.Button(
    root,
    text="Click Me",
    command=on_click,
    font=("Arial", 12),
    fg="white",
    bg="#5b8af0",
    activebackground="#3a6ad4",
    relief="flat",
    padx=16,
    pady=8,
    cursor="hand2",
)
btn.pack(pady=10)

btn.configure(state="disabled")
btn.configure(state="normal")

tk.Button(root, text="Say Hi", command=lambda: print("Hi!")).pack()

is_dark = tk.BooleanVar(value=True)

chk = tk.Checkbutton(
    root,
    text="Dark Mode",
    variable=is_dark,
    command=lambda: print(f"Dark: {is_dark.get()}"),
)
chk.pack()

# ── Radiobutton (share same variable) ──
color = tk.StringVar(value="red")

for opt in ["red", "green", "blue"]:
    tk.Radiobutton(
        root,
        text=opt.capitalize(),
        variable=color,
        value=opt,
        command=lambda: print(f"Selected: {color.get()}"),
    ).pack(anchor="w")

volume = tk.IntVar(value=50)

slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",  # or "vertical"
    variable=volume,
    label="Volume",
    tickinterval=25,
    resolution=5,
    length=300,
    command=lambda v: print(f"Volume: {v}"),
)
slider.pack(pady=10)

print(volume.get())

name_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=name_var,
    width=30,
    font=("Arial", 12),
    bg="#1c2030",
    fg="white",
    insertbackground="white",  # cursor color
    relief="flat",
    show="",  # use "*" for password fields
)
entry.pack(pady=8)
entry.focus_set()  # auto-focus
entry.insert(0, "Placeholder")  # default text
entry.select_range(0, "end")  # select all


# Validation callback
# def validate_num(val):
#     return val.isdigit() or val == ""


def print_name(event=None):
    print(f"Printed name is {name_var.get()}")


root.bind("<Return>", print_name)

# vcmd = root.register(validate_num)
# tk.Entry(root, validate="key", validatecommand=(vcmd, "%P")).pack()

root.mainloop()
