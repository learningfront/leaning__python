# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _damage(self, who_attac):
        return who_attac.damage * (1 - self.armor)

    def attac(self,  who_attac):
        self.health -= self._damage(who_attac)
        print(f'{who_attac.name} наносит {self._damage(who_attac)} урона по {self.name}(HP {self.name}={self.health})')



class Player(Person):
    def __init__(self, name, health, damage, armor, chance_of_crit):
        super().__init__(name, health, damage, armor)
        self.chance_of_crit = chance_of_crit


class Enemy(Person):
    def __init__(self, name, health, damage, armor, elementaly):
        super().__init__(name, health, damage, armor)
        self.elementaly = elementaly


player = Player('Slava', 1000, 50, 0.6, 0.1)
enemy = Enemy('Wolf', 1000, 70, 0.4, 'water-fire')
print(enemy.health)

enemy.attac(player)
print(enemy.health)


def stert_game():
    stack = 'player'
    while True:
        if player.health <= 0:
            print('Враг победил!')
            break
        if enemy.health <= 0:
            print('Игрок победил!')
            break

        if stack == 'player':
            enemy.attac(player)
            stack = 'anemy'
        else:
            player.attac(enemy)
            stack = 'player'


stert_game()
