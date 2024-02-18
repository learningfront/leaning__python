# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {'health': 100,
          'damage': 50}

enemy = {'name': 'player2',
         'health': 1000,
         'damage': 5
         }

player['name'] = input('Введите имя героя: ')


def attack(person1, person2):
    damage = 0
    for i in [player, enemy]:
        if i['name'] == person1:
            damage = i['damage']

    for i in [player, enemy]:
        if i['name'] == person2:
            i['health'] -= damage

    print(player, enemy)


attack('player2', 'slava')


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.



def data_profile(name):

    dict_profile = {}
    with open(f'{name}.txt', 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            key, value = line.split(':')
            if key in ['armor', 'health', 'damage']:
                dict_profile[key] = int(value)
            else:
                dict_profile[key] = value

    return dict_profile


def attack(person1, person2, player, enemy):
    damage = 0
    for i in [player, enemy]:
        if i['name'] == person1:
            damage = i['damage']

    for i in [player, enemy]:
        if i['name'] == person2:
            i['health'] -= damage - i['armor']

    print(player, '\n',  enemy, '\n')


def game(play1, play2):
    pl1, pl2 = data_profile(play1), data_profile(play2)
    print(pl1, '\n' , pl2, '\n')

    while True:
        if pl1['health'] <= 0:
            print(play1, ' Погиб')
            break
        else:
            attack(play1, play2, pl1, pl2)

        if pl2['health'] <= 0:
            print(play2, ' Погиб')
            break
        else:
            attack(play2, play1, pl2, pl1)


game('slava', 'player2')








