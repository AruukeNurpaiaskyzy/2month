# # Создать класс MagicCalculator с атрибутами number_1 и number_2, в котором будут реализованы магические методы для арифметических вычислений
# #  между аргументами класса  MagicCalculator ( +, -, *, /, // )

class MagicCalcultor:
    def __init__(self, numbers_1, numbers_2):
        self.numbers_1 = numbers_1
        self.numbers_2 = numbers_2

    def __add__(self, other):
        result = self.numbers_1 + self.numbers_2
        return f"Результат сложения: {result}"

    
#     def __sub__(self, other):
#         result = self.numbers_1 - other.numbers_1
#         return f"Результат вычетания: {result}"
    
#     def __mul__(self, other):
#         result = self.numbers_1 * other.numbers_1
#         return f"Результат умножения: {result}"

    
#     def __truediv__(self, other):
#         result = self.numbers_1 / other.numbers_1
#         return f"Результат деления: {result}"

    

# num1 = MagicCalcultor(10, 10)
# num2 = MagicCalcultor(12, 12)
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# Доп задание:

# Вы разрабатываете программу для управления библиотекой книг. Вам необходимо создать класс Book, который будет представлять отдельную книгу. Книги
#  могут иметь различные атрибуты, такие как название, автор, год издания и т. д. Кроме того, вы хотите, чтобы книги можно было сравнивать между собой на основе их года издания.

# Ваша задача - создать класс Book, который реализует методы для сравнения книг между собой по году издания, а также выводить информацию о книге в удобном формате.

# Условия:

# Реализуйте методы lt, le, gt, ge, eq, ne для сравнения книг между собой на основе года издания.
# Реализуйте метод str для вывода информации о книге в удобном формате.


# class Book:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year

#     def __str__(self):
#         return f"Названия книги: {self.name}, Автор книги: {self.author}, год выпуска книги: {self.year}"

#     def book(self):
#         print(f"Названия книги: {self.name}, Автор книги: {self.author}, год выпуска книги: {self.year}")

#     def __gt__(self, other):
#         return self.year > other.year

#     def __lt__(self, other):
#         return self.year < other.year

#     def __eq__(self, other):
#         return self.year == other.year 

#     def __ne__(self, other):
#         return self.year != other.year

#     def __ge__(self, other):
#         return self.year >= other.year

#     def __le__(self, other):
#         return self.year <= other.year


# book1 = Book("Война и мир", "Лев Толстой", 1869)
# book2 = Book("Мцыри", "Лермантов", 1840)
# book3 = Book("Капита́нская до́чка", "Пушкин", 1836)

# book1.book()

# book2.book()

# book3.book()

# print(book1 > book2 > book3)
# print(book1 < book2 < book3)
# print(book1 == book2 == book3)
# print(book1 != book2 != book3)
# print(book1 >= book2 >= book3)
# print(book1 <= book2 <= book3)