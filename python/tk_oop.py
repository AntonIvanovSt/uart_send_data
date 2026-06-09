import tkinter as tk


class CounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CounterApp")
        self.geometry("640x480")
        self.resizable(False, False)
        self.configure(bg="#0d0f14")

        self.count = 0
        self.count_var = tk.StringVar(value="0")

        self._build_ui()
        self._bind_keys()

    def _build_ui(self):
        tk.Label(
            self, text="Counter", font=("Arial", 14), fg="#8892a4", bg="#0d0f14"
        ).pack(pady=(20, 5))
        tk.Label(
            self,
            textvariable=self.count_var,
            font=("Arial", 24, "bold"),
            fg="#5b8af0",
            bg="#0d0f14",
        ).pack()

        btn_frame = tk.Frame(self, bg="#0d0f14")
        btn_frame.pack(pady=15)

        for text, cmd in [
            ("-", self.decrement),
            ("Reset", self.reset),
            ("+", self.increment),
        ]:
            tk.Button(
                btn_frame,
                text=text,
                command=cmd,
                font=("Arial", 14),
                width=5,
                bg="#1c2030",
                fg="white",
                relief="flat",
                cursor="hand2",
            ).pack(side="left", padx=4)

    def _bind_keys(self):
        self.bind("<Up>", lambda e: self.increment())
        self.bind("<Down>", lambda e: self.decrement())
        self.bind("<r>", lambda e: self.reset())

    def increment(self):
        self.count += 1
        self.count_var.set(str(self.count))

    def decrement(self):
        self.count -= 1
        self.count_var.set(str(self.count))

    def reset(self):
        self.count = 0
        self.count_var.set("0")


if __name__ == "__main__":
    app = CounterApp()
    app.mainloop()
