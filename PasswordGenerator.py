import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.digits_chars = string.digits
        self.special_chars = "!@#$%^&*()_+-"

    def generate(self, num_lower, num_upper, num_digits, num_special):
        # Простейшая версия: склеиваем без перемешивания
        lower_part = [random.choice(self.lowercase_chars) for _ in range(num_lower)]
        upper_part = [random.choice(self.uppercase_chars) for _ in range(num_upper)]
        digits_part = [random.choice(self.digits_chars) for _ in range(num_digits)]
        special_part = [random.choice(self.special_chars) for _ in range(num_special)]
        return ''.join(lower_part + upper_part + digits_part + special_part)