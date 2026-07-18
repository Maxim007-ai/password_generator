import unittest
import string
from PasswordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    #Набор тестов для класса PasswordGenerator.

    def setUp(self):
        #Создаёт экземпляр генератора перед каждым тестом.
        self.gen = PasswordGenerator()

    def test_total_length(self):
        #Проверка общей длины пароля.
        pwd = self.gen.generate(3, 4, 2, 5)   # 3+4+2+5 = 14
        self.assertEqual(len(pwd), 14,
                         "Общая длина пароля должна равняться сумме запрошенных символов")


    def test_category_distribution(self):
        #Проверка, что в смешанном пароле не потеряны символы категорий.
        pwd = self.gen.generate(3, 4, 2, 5)
        lower_cnt = sum(1 for c in pwd if c in self.gen.lowercase_chars)
        upper_cnt = sum(1 for c in pwd if c in self.gen.uppercase_chars)
        dig_cnt   = sum(1 for c in pwd if c in self.gen.digits_chars)
        spec_cnt  = sum(1 for c in pwd if c in self.gen.special_chars)
        self.assertGreaterEqual(lower_cnt, 3, "Строчных букв меньше запрошенного")
        self.assertGreaterEqual(upper_cnt, 4, "Заглавных букв меньше запрошенного")
        self.assertGreaterEqual(dig_cnt,   2, "Цифр меньше запрошенного")
        self.assertGreaterEqual(spec_cnt,  5, "Спецсимволов меньше запрошенного")

    def test_characters_validity(self):
        #Все символы пароля принадлежат разрешённым наборам.
        pwd = self.gen.generate(2, 2, 2, 2)
        all_allowed = (self.gen.lowercase_chars + self.gen.uppercase_chars +
                       self.gen.digits_chars + self.gen.special_chars)
        for ch in pwd:
            self.assertIn(ch, all_allowed,
                          f"Символ '{ch}' не входит в допустимые множества")

    def test_empty_password(self):
        #Генерация с нулевыми параметрами даёт пустую строку.
        pwd = self.gen.generate(0, 0, 0, 0)
        self.assertEqual(pwd, "", "Пароль с нулями должен быть пустым")

    def test_randomness_basic(self):
        #Многократная генерация не должна давать одинаковые пароли.
        passwords = set()
        for _ in range(50):
            pwd = self.gen.generate(2, 2, 2, 2)
            passwords.add(pwd)
        # При 50 вызовах практически невероятно получить менее 2 уникальных значений
        self.assertGreater(len(passwords), 1,
                           "Слишком часто повторяются одинаковые пароли – вероятна ошибка случайности")

if __name__ == '__main__':
    unittest.main()