import tkinter as tk

root = tk.Tk()
root.title("Grid Login form")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=8, sticky="e")

user_entry = tk.Entry(root, width=25)
pass_entry = tk.Entry(root, width=25, show="*")  # show="*" for password
user_entry.grid(row=0, column=1, padx=10)
pass_entry.grid(row=1, column=1, padx=10)

tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2, pady=10)

root.columnconfigure(1, weight=1)

root.mainloop()
