import tkinter as tk
import tkinter.font as tkFont


class Calculate:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

        if op == "+":
            self.result = self.addition()
        elif op == "-":
            self.result = self.minus()
        elif op == "*":
            self.result = self.times()
        elif op == "/":
            self.result = self.divine()

    def addition(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def times(self):
        return self.a * self.b

    def divine(self):
        if self.b != 0:
            return self.a / self.b
        else:
            raise ValueError("0 cannot be on the denominator")


class CalculatorApp:
    def __init__(self, master):
        self.values = {"a": None, "b": None, "op": None}

        self.master = master
        self.dimension = 700
        self.master.geometry(f"{self.dimension}x{self.dimension}")
        self.master.title("Calculator")
        self.layout = tk.Frame(self.master, width=self.dimension, height=self.dimension)

        self.fontStyle = tkFont.Font(family="Courier", size=40)

        # LED Display
        self.display = tk.Label(self.layout, text=0, bg="white", height=2, anchor="e", bd=1, relief="solid", font=self.fontStyle, padx=self.dimension // 3)
        self.display.pack_propagate(False)
        self.display.grid(row=1, column=1)

        self.layout.grid(row=1, column=1)

        # 0-9 Numpad
        self.numpad_layout = tk.Frame(self.layout)
        self.count = 1
        for row in range(3):
            for col in range(3):
                self.cell = tk.Button(self.numpad_layout, width=10, height=5, text=self.count, font=("Courier", 12), borderwidth=1, relief="solid",
                                      bg="white")
                self.count += 1
                self.cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        self.numpad_layout.grid(row=2, column=1, columnspan=1)

        # Operation buttons
        self.operation_layout = tk.Frame(self.layout)

        self.clear_button = tk.Button(self.operation_layout, text="C", width=4, height=2, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.clear_button.grid(row=1, column=1, pady=5)

        self.add_button = tk.Button(self.operation_layout, text="+", width=4, height=2, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.add_button.grid(row=2, column=1, pady=5)

        self.minus_button = tk.Button(self.operation_layout, text="-", width=4, height=2, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.minus_button.grid(row=3, column=1, pady=5)

        self.times_button = tk.Button(self.operation_layout, text="*", width=4, height=2, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.times_button.grid(row=4, column=1, pady=5)

        self.divine_button = tk.Button(self.operation_layout, text="/", width=4, height=2, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.divine_button.grid(row=5, column=1, pady=5)

        self.equal_button = tk.Button(self.operation_layout, text="=", width=4, height=5, font=("Courier", 12), borderwidth=1, relief="solid", bg="white", fg="blue")
        self.equal_button.grid(row=6, column=1, pady=5)

        self.operation_layout.grid(row=2, column=2)

        self.master.bind("<Button-1>", self.button_press)

    def button_press(self, event):
        widget = self.master.winfo_containing(event.x_root, event.y_root)
        if widget in self.numpad_layout.winfo_children() and type(widget) is tk.Button:
            self.display.configure(text=int(str(self.display["text"]) + str(widget["text"])))

        elif widget in self.operation_layout.winfo_children() and type(widget) is tk.Button:
            if widget["text"] == "=" :
                self.values["b"] = self.display["text"]
                result = Calculate(self.values["a"], self.values["b"], self.values["op"]).result
                self.display.configure(text=result)
                self.clear_values()
                self.values["a"] = result
            elif widget["text"] == "C":
                self.clear_values()
                self.display.configure(text=0)
            else:
                if not self.values["a"]:
                    self.values["a"] = self.display["text"]
                else:
                    self.values["b"] = self.display["text"]

                self.values["op"] = widget["text"]
                self.display.configure(text=0)
        # print(self.values)

    def clear_values(self):
        self.values["a"] = None
        self.values["b"] = None
        self.values["op"] = None


if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
