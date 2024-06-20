from lesson6 import Backend
class Geeks (Backend):
    def direction(self):
        print(f"мы изучаем {self.django}, {self.docker} по направлению бекгенд")
py = Geeks("Alaget.kg", "Docker")
py.direction()