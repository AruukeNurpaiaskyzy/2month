import sqlite3

conn = sqlite3.connect('game.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS game_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    description TEXT NOT NULL
)
''')

def player():
    start = int(input('Начать игру? да - 1, нет - 2\n'))
    if start == 1:
        print("игра началась!")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('player', 'игра началась!'))
    elif start == 2:
        print("игра приостановлена!")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('player', 'игра приостановлена!'))
    else:
        print("такой команды нет!")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('player', 'неизвестная команда'))
    conn.commit()

def adjust_rule():
    adjuster = int(input('повернуть направо?: да - 1, повернуть налево нет - 2\n'))
    if adjuster == 1:
        print("повернуть направо!")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('adjust_rule', 'повернуть направо!'))
    else:
        print("иначе такой команды нету")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('adjust_rule', 'неизвестная команда'))
    conn.commit()

def game_is_over():
    lose = int(input('проиграли?: да - 1, выиграли - 2\n'))
    if lose == 1:
        print("проиграли!")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('game_is_over', 'проиграли!'))
    else:
        print("иначе такой команды нету")
        cursor.execute("INSERT INTO game_log (action, description) VALUES (?, ?)", ('game_is_over', 'неизвестная команда'))
    conn.commit()

def main():
    player()
    adjust_rule()
    game_is_over()
    
if __name__ == '__main__':
    main()

conn.close()
