import sqlite3

# Создание соединения с базой данных и курсора
connect = sqlite3.connect("mentors.db")
cursor = connect.cursor()

# Создание таблицы mentors с необходимыми полями
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR (30) NOT NULL,
    last_name VARCHAR (30) NOT NULL,
    age INT DEFAULT NULL,
    address VARCHAR (50), 
    email VARCHAR (30),
    month_group VARCHAR(30),
    study_group VARCHAR(30),
    coins INTEGER DEFAULT 0
)
""")

class Mentors:
    def __init__(self):
        self.connect = connect
        self.cursor = cursor

    def register(self):
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        age = int(input("Введите возраст: "))
        address = input("Введите адрес: ")
        email = input("Введите почту: ")
        month_group = input("Введите группу месяца: ")
        study_group = input("Введите учебную группу: ")

        self.cursor.execute("SELECT * FROM mentors WHERE first_name = ?", (first_name,))
        mentor = self.cursor.fetchone()

        if mentor:
            print("Already exists - Вы уже проходили регистрацию")
        else:
            self.cursor.execute("""
                INSERT INTO mentors (first_name, last_name, age, address, email, month_group, study_group, coins)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, age, address, email, month_group, study_group, 0))
            print("Вы успешно прошли регистрацию!")

        self.connect.commit()

    def all_mentors(self):
        self.cursor.execute("SELECT * FROM mentors")
        mentors = self.cursor.fetchall()
        for mentor in mentors:
            print(mentor)

    def plus_mentor_coins(self):
        id = int(input("Введите id ментора: "))
        new_coins = int(input("Введите количество коинов для добавления: "))

        self.cursor.execute("UPDATE mentors SET coins = coins + ? WHERE id = ?", (new_coins, id))
        self.connect.commit()
        print("Коины успешно добавлены!")

    def minus_mentor_coins(self):
        id = int(input("Введите id ментора: "))
        withdraw_coins = int(input("Введите количество коинов для снятия: "))

        self.cursor.execute("SELECT coins FROM mentors WHERE id = ?", (id,))
        current_coins = self.cursor.fetchone()[0]

        if current_coins >= withdraw_coins:
            self.cursor.execute("UPDATE mentors SET coins = coins - ? WHERE id = ?", (withdraw_coins, id))
            self.connect.commit()
            print("Коины успешно сняты!")
        else:
            print("Недостаточно коинов для снятия")

    def delete_mentor(self):
        id = int(input("Введите id ментора: "))
        self.cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
        self.connect.commit()
        print("Ментор успешно удален")

    def main(self):
        while True:
            print("Выберите действие: ")
            print("""0-Выйти, 1-Регистрация, 2-Инфо всех менторов
3-Добавление коинов, 4-Снятие коинов,
5-Удаление ментора""")
            
            choice = int(input("Выберите цифру: "))
            if choice == 0:
                break
            elif choice == 1:
                self.register()
            elif choice == 2:
                self.all_mentors()
            elif choice == 3:
                self.plus_mentor_coins()
            elif choice == 4:
                self.minus_mentor_coins()
            elif choice == 5:
                self.delete_mentor()

mentors = Mentors()
mentors.main()