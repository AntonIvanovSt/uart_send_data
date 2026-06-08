import tkinter as tk

root = tk.Tk()

root.title("Window Config Demo")

root.geometry("600x400+100+100")

root.minsize(300, 200)
root.maxsize(1200, 800)

root.resizable(True, True)

root.configure(bg="#1c2030")

tk.Label(
    root, text="Hello, Tkinter", font=("Arial", 24, "bold"), fg="#ffffff", bg="#1c2030"
).pack(pady=50)

tk.Label(root, text="Top", bg="#5b8af0").pack(side="top", fill="x")
tk.Label(root, text="Left", bg="#7c5bf0").pack(side="left", fill="y")
tk.Label(root, text="Center", bg="#3ecf8e").pack(expand=True)

root.eval("tk::PlaceWindow . center")

root.mainloop()
