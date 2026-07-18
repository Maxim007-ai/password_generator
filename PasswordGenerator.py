import random
import string
import tkinter as tk
class PasswordGenerator:
    def __init__(self):
        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.digits_chars = string.digits
        self.special_chars = "!@#$%^&*()_+-"

    def generate(self, num_lower, num_upper, num_digits, num_special):
        lower_part = [random.choice(self.lowercase_chars) for _ in range(num_lower)]
        upper_part = [random.choice(self.uppercase_chars) for _ in range(num_upper)]
        digits_part = [random.choice(self.digits_chars) for _ in range(num_digits)]
        special_part = [random.choice(self.special_chars) for _ in range(num_special)]
        password_list = lower_part + upper_part + digits_part + special_part
        random.shuffle(password_list)
        return ''.join(password_list)

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")
        self.gen = PasswordGenerator()
        # простейшая кнопка
        btn = tk.Button(root, text="Сгенерировать", command=self.on_generate)
        btn.pack()
        self.result = tk.Label(root, text="")
        self.result.pack()

    def on_generate(self):
        pwd = self.gen.generate(3,2,2,2)
        self.result.config(text=pwd)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()