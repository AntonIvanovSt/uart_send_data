import tkinter as tk

root = tk.Tk()

root.title("Events")
root.geometry("640x480")

status = tk.StringVar(value="Waiting for events...")
tk.Label(root, textvariable=status, font=("Arial", 14)).pack(pady=30)

canvas = tk.Canvas(root, bg="#1c2030", width=360, height=200)
canvas.pack()


def on_click(event):
    status.set(f"Clicked at ({event.x}, {event.y})")
    canvas.create_oval(
        event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="#5b8af0"
    )


def on_key(event):
    status.set(f"Key pressed: {event.keysym} (char: {event.char!r})")


def on_enter(event):
    status.set("Mouse entered canvas")


canvas.bind("<Button-1>", on_click)
root.bind("<Key>", on_key)
canvas.bind("<Enter>", on_enter)
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
