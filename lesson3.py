# "инкопсуляция"
class Phone:
    def __init__(self, brand, password, gallery):
        self.brand = brand
        self._password = password 
        self.__gallery = gallery
        def info(self):
            print(f"Модель телефона")
passwords = [1234, "0000"]
phone = Phone("iphone", passwords, "gallereya")
print(phone.brand)
print(phone._password)
print(phone.__gallery)
