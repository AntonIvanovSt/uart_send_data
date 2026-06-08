import tkinter as tk

root = tk.Tk()
root.title("Hello world")
root.title("640x480")

label = tk.Label(root, text="Hello, Tkinter", font=("Arial", 24, "bold"), fg="#5b8af0")

label.pack(pady=50)

root.mainloop()
