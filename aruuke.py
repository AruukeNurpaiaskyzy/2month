class Person:
    def __init__ (self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def info(self):
        print(f" полное имя {self.fullname}, также возраст {self.age}, конечно же {self.is_married}")

info1 = Person("Aruuke", 18, "нет")
info1.info()

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary
    def salary_experience(self):
        for 
         
      

              



        