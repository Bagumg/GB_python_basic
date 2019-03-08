#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random

# player_card = [sorted(random.randint(1, 90) for i in range(0,9)) for j in range(0,3)]

barrel = list(range(1, 90))


def generate_card():
    card = [random.sample(barrel, 9) for i in range(0, 3)]
    for i in card:
        for j in range(4):
            while i.count('') != 4:
                random.shuffle(i)
                i[j] = ''
    return card


def next_barrel():
    next_barrel = random.sample(barrel, 1)
    return next_barrel


def turn():
    for i in range(len(barrel)):
        if barrel[i] == current_barrel[0]:
            barrel.remove(barrel[i])
            break
    return barrel


def mark():
    for i in range(len((player1_card))):
        if current_barrel[0] in player1_card[i]:
            player1_card[i].remove(current_barrel[0])
            turn()


player1_card = generate_card()
computer_card = generate_card()
current_barrel = next_barrel()
print('Начнём?')
answer = input('Y/N')
while answer == 'y' or answer == 'Y':
    print()
    print('Карточка первого игрока:')
    for i in player1_card:
        print(i)
    print()
    print('Карточка компьютера:')
    for i in computer_card:
        print(i)
    print()
    current_barrel = next_barrel()
    for i in range(3):
        if current_barrel[0] in computer_card[i]:
            player1_card[i].remove(current_barrel[0])
    if len(computer_card[0]) == 4 and len(computer_card[1]) == 4 and len(computer_card[2]) == 4:
        print('Ха-ха, кусок мяса, я победил!')
        print('Поцелуй мой блестящий, металлический зад!')
        break
    print('Выпадает бочонок номер', current_barrel)
    print('Игрок, ваша карточка')
    for i in player1_card:
        print(i)
    print()
    player_answer = input('Желаете зачеркнуть? Y/N')
    if player_answer == 'Y' or player_answer == 'y':
        if current_barrel[0] not in player1_card[0] and current_barrel[0] not in player1_card[1] and current_barrel[0] not in player1_card[2]:
            print('Этого числа нет в вашей карточке. Вы проиграли!')
            break
        mark()
    else:
        if current_barrel[0] in player1_card[0]:
            print('Внимательнее, число есть в вашей карточке. Вы проиграли!')
            break
        if current_barrel[0] in player1_card[1]:
            print('Внимательнее, число есть в вашей карточке. Вы проиграли!')
            break
        if current_barrel[0] in player1_card[2]:
            print('Внимательнее, число есть в вашей карточке. Вы проиграли!')
            break
    if len(player1_card[0]) == 4 and len(player1_card[1]) == 4 and len(player1_card[2]) == 4:
        print('Вы победили!')
        break
    print('Игрок, ваша карточка')
    for i in player1_card:
        print(i)
    turn()
print('Жаль, игра-то хорошая!')