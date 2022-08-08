# Создайте программу для игры в "Крестики-нолики".

from random import randint


def PrintPole(field):
    for i in range(0, len(field)):
        for i2 in range(0, len(field[i])):
            print(field[i][i2], end=' ')
        print()


def Move(hod, field, who_move):
    if hod == 1 and who_move == 1 and CheckMove(hod, field):
        field[0][0] = 'x'
        who_move = -1
    elif hod == 2 and who_move == 1 and CheckMove(hod, field):
        field[0][1] = 'x'
        who_move = -1
    elif hod == 3 and who_move == 1 and CheckMove(hod, field):
        field[0][2] = 'x'
        who_move = -1
    elif hod == 4 and who_move == 1 and CheckMove(hod, field):
        field[1][0] = 'x'
        who_move = -1
    elif hod == 5 and who_move == 1 and CheckMove(hod, field):
        field[1][1] = 'x'
        who_move = -1
    elif hod == 6 and who_move == 1 and CheckMove(hod, field):
        field[1][2] = 'x'
        who_move = -1
    elif hod == 7 and who_move == 1 and CheckMove(hod, field):
        field[2][0] = 'x'
        who_move = -1
    elif hod == 8 and who_move == 1 and CheckMove(hod, field):
        field[2][1] = 'x'
        who_move = -1
    elif hod == 9 and who_move == 1 and CheckMove(hod, field):
        field[2][2] = 'x'
        who_move = -1
    elif hod == 1 and who_move == -1 and CheckMove(hod, field):
        field[0][0] = '0'
        who_move = 1
    elif hod == 2 and who_move == -1 and CheckMove(hod, field):
        field[0][1] = '0'
        who_move = 1
    elif hod == 3 and who_move == -1 and CheckMove(hod, field):
        field[0][2] = '0'
        who_move = 1
    elif hod == 4 and who_move == -1 and CheckMove(hod, field):
        field[1][0] = '0'
        who_move = 1
    elif hod == 5 and who_move == -1 and CheckMove(hod, field):
        field[1][1] = '0'
        who_move = 1
    elif hod == 6 and who_move == -1 and CheckMove(hod, field):
        field[1][2] = '0'
        who_move = 1
    elif hod == 7 and who_move == -1 and CheckMove(hod, field):
        field[2][0] = '0'
        who_move = 1
    elif hod == 8 and who_move == -1 and CheckMove(hod, field):
        field[2][1] = '0'
        who_move = 1
    elif hod == 9 and who_move == -1 and CheckMove(hod, field):
        field[2][2] = '0'
        who_move = 1
    return field, who_move


def CheckGame(field, game_status, winner):
    if field[0][0] == field[0][1] == field[0][2] == 'x' or field[0][0] == field[1][1] == field[2][2] == 'x' \
            or field[0][0] == field[1][0] == field[2][0] == 'x' or field[0][0] == field[1][0] == field[2][0] == 'x' \
            or field[0][2] == field[1][2] == field[2][2] == 'x' or field[0][0] == field[1][1] == field[2][2] == 'x' \
            or field[0][2] == field[1][1] == field[2][0] == 'x' or field[2][0] == field[2][1] == field[2][2] == 'x':
        game_status = False
        winner = 1
    elif field[0][0] == field[0][1] == field[0][2] == '0' or field[0][0] == field[1][1] == field[2][2] == '0' \
            or field[0][0] == field[1][0] == field[2][0] == '0' or field[0][0] == field[1][0] == field[2][0] == '0' \
            or field[0][2] == field[1][2] == field[2][2] == '0' or field[0][0] == field[1][1] == field[2][2] == '0' \
            or field[0][2] == field[1][1] == field[2][0] == '0' or field[2][0] == field[2][1] == field[2][2] == '0':
        game_status = False
        winner = 0
    return game_status, winner


def CheckMove(move, field):
    check_move = None
    if move == 1:
        if field[0][0] == '_':
            check_move = True
    if move == 2:
        if field[0][1] == '_':
            check_move = True
    if move == 3:
        if field[0][2] == '_':
            check_move = True
    if move == 4:
        if field[1][0] == '_':
            check_move = True
    if move == 5:
        if field[1][1] == '_':
            check_move = True
    if move == 6:
        if field[1][2] == '_':
            check_move = True
    if move == 7:
        if field[2][0] == '_':
            check_move = True
    if move == 8:
        if field[2][1] == '_':
            check_move = True
    if move == 9:
        if field[2][2] == '_':
            check_move = True
    return check_move


user_name = input("Введите своё имя: ")
pc_name = 'Компьютер'
pole = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
game = True
win = -1
who = 0

first_move = randint(0, 1)
if first_move == 0:
    print(f'Случайным образом решено, что первым ходит {pc_name}.')
    who = -1
else:
    print(f'Случайным образом решено, что первым ходит {user_name}.')
    who = 1

while game != False:
    if who == 1:
        PrintPole(pole)
        while who == 1:
            user_move = int(input(f'{user_name}, выберете ячейку от 1 до 9: '))
            pole, who = Move(user_move, pole, who)
            game, win = CheckGame(pole, game, win)
    elif who == -1:
        while who == -1:
            pc_move = randint(1, 10)
            pole, who = Move(pc_move, pole, who)
            print(f'Компьютер выбрал ячейку {pc_move}.')
            game, win = CheckGame(pole, game, win)

else:
    if win == 1:
        PrintPole(pole)
        print(f'Игра закончена! Победил {user_name}.')

    elif win == 0:
        PrintPole(pole)
        print(f'Игра закончена! Победил {pc_name}.')