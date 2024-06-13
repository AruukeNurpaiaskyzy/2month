# #1. Создать класс Person с атрибутами fullname, age, is_married

# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
    
#     def introduce_myself(self):
#         print(f"my name is {self.fullname}, my age  {self.age},  i am {self.is_married}")

# eliza = Person("Eliza", 17, 'not married')   
# eliza.introduce_myself()
 
# # 3. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом объекта experience.
# # . Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.

# # 3. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату


# class Teacher(Person):
#     def __init__(self, fullname, age, is_married):
#         super().__init__(fullname, age, is_married, experience)
#         self.experience = experience
#         self.salary = 0 
    
#     def info(self):
#         print(f"my name is {self.fullname}, my experience of work {self.experience} year")

#     def salary_check(self):
#         for i in range(self.experience):
#             self.salary += 3000
#         print(f"Моя зарплата {self.salary}")

    

# eliza = Teacher("Eliza", 17, 'not married', 3)
# eliza.info()
# eliza.salary_check()
# eliza.introduce_myself()


       



    











