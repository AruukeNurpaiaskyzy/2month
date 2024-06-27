
def player():
    start = int(input('Начать игру? да - 1, нет - 2\n'))
    is_start = True
    if start == 1:
        is_start == True
        print("игра началась!")  
    elif start == 2: 
        print("игра приостановлена!")
    else:
        print("такой команды нет!")


def adjust_rule():
    adjuster = int(input('повернуть напрво?: да - 1, повернуть налево нет - 2'))
    if adjuster == 1:
        print("повернуть направо!")  
    
    else:
        print("иначе такой команды нету")



def game_is_over():
    lose= int(input('проиграли?: да - 1, выйиграли - 2'))
    if lose == 1:
        print("проиграли!")  
    
    else:
        print("иначе такой команды нету")
player()
adjust_rule()
game_is_over()




