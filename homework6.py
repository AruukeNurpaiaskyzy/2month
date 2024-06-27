from lesson6.6 import Game
class Sharlotka(Game):
    def info(self):
        print(f"графика {self.graphic}, число героев {self.the_numbers_of_characters}, оценка {self.marks/100}, уровни {self.levels}")
game = Sharlotka ("3D", 20, 0, "beginner, middle, advanced" )
game.info()
