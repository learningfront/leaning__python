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


class Card:
    def __init__(self, name):
        self.name = name

    def create_card(self):
        card = [[], [], []]
        all_num = []
        line = 3
        column = 9
        # Заполняем 3 ряда по 9 цифр уникальными рандомными цифрами.
        for i in range(line):
            for j in range(column):
                while True:
                    rand_num = random.randint(1, 90)
                    if rand_num in all_num:
                        continue
                    else:
                        all_num.append(rand_num)
                        card[i].insert(j, rand_num)
                        break
            # Сортируем каждый ряд после заполнения
            card[i].sort()
            # Удаляем по 4 цифры в каждом ряду, заменяя их на два пробела
            for x in range(4):
                while True:
                    rand_elem = random.choice(card[i])
                    if rand_elem != '  ':
                        card[i][card[i].index(rand_elem)] = '  '
                        break
        return card

    def print_card(self, card):
        str_line = ''
        print('__________________________')
        print(f'-----------{self.name}----------')
        for i in card:
            for j in i:
                if j != '  ' and j != '--' and j < 10:
                    str_line += '0' + str(j) + ' '
                else:
                    str_line += str(j) + ' '

            print(str_line)
            str_line = ''
        print('--------------------------')

    def get_all_num_card(self, card):
        all_num = []
        for i in card:
            for j in i:
                all_num.append(j)

        all_num = list(set(all_num))
        all_num.remove('  ')
        return all_num

    def check_barrel(self, card, barrel):
        if barrel in self.get_all_num_card(card):
            return True
        return False

    def delite_num(self, card, all_num, barrel):
        if barrel in all_num:
            all_num.remove(barrel)

            for i in card:
                for j in i:
                    if j == barrel:
                        card[card.index(i)][i.index(j)] = '--'


class Barrel:

    def __init__(self):
        self.list_barrel = []

    def create_barrel(self, list_barrel):
        while True:
            barrel_num = random.randint(1, 90)
            if barrel_num in list_barrel:
                continue
            else:
                self.list_barrel.append(barrel_num)
                return barrel_num

    def print_list_barrel(self):
        print(f'Уже были {len(self.list_barrel)}: \n {self.list_barrel}')


class GameLoto:
    def __init__(self, name_player, computer):
        self.player = Card(name_player)
        self.computer = Card(computer)
        self.barrel = Barrel()

    def start(self):
        card_player = self.player.create_card()
        card_computer = self.computer.create_card()
        all_num_card_player = self.player.get_all_num_card(card_player)
        all_num_card_computer = self.computer.get_all_num_card(card_computer)

        while True:
            if len(all_num_card_player) == 0:
                print(f'{self.player.name} победил!')
                break
            if len(all_num_card_computer) == 0:
                print(f'{self.computer.name} победил!')
                break

            barrel_this_turn = self.barrel.create_barrel(self.barrel.list_barrel)
            print(f'Выпал бочонок {barrel_this_turn}')
            self.player.print_card(card_player)
            self.computer.print_card(card_computer)

            solution = input('Введите y или n, чтобы зачеркнуть цифру или продолжить: -->  ')

            if solution == 'y' and self.player.check_barrel(card_player, barrel_this_turn) == False:
                print('Бля дурак, нету такого числа на твоей карточки')
                print(f'{self.computer.name} победил!')
                break
            elif solution == 'n' and self.player.check_barrel(card_player, barrel_this_turn) == True:
                print('Проебал число, оно было на карточке ')
                print(f'{self.computer.name} победил!')
                break
            else:
                self.player.delite_num(card_player, all_num_card_player, barrel_this_turn)
                self.computer.delite_num(card_computer, all_num_card_computer, barrel_this_turn)

if __name__ == '__main__':
    game = GameLoto('slava', 'komp ')
    game.start()
