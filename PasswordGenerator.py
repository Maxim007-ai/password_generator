import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:

    #Класс, реализующий логику генерации пароля.

    def __init__(self):
        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.digits_chars = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

    def generate(self, num_lower, num_upper, num_digits, num_special):

        # Генерирует пароль из заданного количества символов каждой категории
        # и возвращает его в виде строки с перемешанными символами.

        # Генерация случайных символов нужной длины для каждой категории
        lower_part = [random.choice(self.lowercase_chars) for _ in range(num_lower)]
        upper_part = [random.choice(self.uppercase_chars) for _ in range(num_upper)]
        digits_part = [random.choice(self.digits_chars) for _ in range(num_digits)]
        special_part = [random.choice(self.special_chars) for _ in range(num_special)]

        # Объединение всех символов
        password_list = lower_part + upper_part + digits_part + special_part

        # Перемешивание для удаления предсказуемого порядка
        random.shuffle(password_list)

        return ''.join(password_list)

class PasswordGeneratorGUI:

    #Графический интерфейс на основе tkinter."

    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.generator = PasswordGenerator()

        # Заголовок
        title = tk.Label(root, text="Генератор паролей 2 задание", font=("Arial", 14, "bold"))
        title.pack(pady=10)

        # Поля ввода количества символов
        self.create_input("Строчные буквы (a-z):", "lower", 0)
        self.create_input("Заглавные буквы (A-Z):", "upper", 1)
        self.create_input("Цифры (0-9):", "digits", 2)
        self.create_input("Специальные символы:", "special", 3)

        # Кнопка генерации
        gen_btn = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password,
                            bg="#4CAF50", fg="white", font=("Arial", 11))
        gen_btn.pack(pady=15)

        # Поле вывода пароля
        self.result_var = tk.StringVar()
        result_frame = tk.Frame(root)
        result_frame.pack(pady=5)
        result_label = tk.Label(result_frame, text="Ваш пароль:", font=("Arial", 11))
        result_label.pack(side=tk.LEFT, padx=5)
        result_entry = tk.Entry(result_frame, textvariable=self.result_var, width=35,
                                font=("Arial", 11), state='readonly')
        result_entry.pack(side=tk.LEFT)

        # Кнопка копирования (дополнительное удобство)
        copy_btn = tk.Button(root, text="Копировать в буфер", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def create_input(self, label_text, attr_name, row):
        # Создаёт строку с надписью и полем ввода.
        frame = tk.Frame(self.root)
        frame.pack(pady=3, padx=20, anchor='w')
        label = tk.Label(frame, text=label_text, width=30, anchor='w')
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=8)
        entry.pack(side=tk.LEFT)
        setattr(self, f"{attr_name}_entry", entry)

    def get_int(self, entry_widget, field_name):

        # Безопасное получение целого числа из поля ввода.

        try:
            val = entry_widget.get().strip()
            if val == "":
                return 0
            return int(val)
        except ValueError:
            messagebox.showerror("Ошибка ввода",
                                 f"Поле '{field_name}' должно содержать целое неотрицательное число.")
            return None

    def generate_password(self):

        # Обработчик нажатия кнопки генерации.

        lower = self.get_int(self.lower_entry, "Строчные буквы")
        if lower is None: return
        upper = self.get_int(self.upper_entry, "Заглавные буквы")
        if upper is None: return
        digits = self.get_int(self.digits_entry, "Цифры")
        if digits is None: return
        special = self.get_int(self.special_entry, "Специальные символы")
        if special is None: return

        total = lower + upper + digits + special
        if total == 0:
            messagebox.showwarning("Пустой пароль", "Укажите хотя бы один символ любого типа.")
            return

        try:
            password = self.generator.generate(lower, upper, digits, special)
            self.result_var.set(password)
        except Exception as e:
            messagebox.showerror("Ошибка генерации", f"Не удалось создать пароль: {e}")

    def copy_to_clipboard(self):

        # Копирует пароль в буфер обмена.

        pwd = self.result_var.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Готово", "Пароль скопирован в буфер обмена.")
        else:
            messagebox.showwarning("Нет пароля", "Сначала сгенерируйте пароль.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
