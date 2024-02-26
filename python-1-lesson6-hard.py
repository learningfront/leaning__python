# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.



class Product:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Plastic(Product):
    def __init__(self, name, color, tipe):
        super().__init__(name, color)
        self.tipe = tipe


class Glass(Product):
    def __init__(self, name, color, tipe):
        super().__init__(name, color)
        self.tipe = tipe
class Tree(Product):
    def __init__(self, name, color, tipe):
        super().__init__(name, color)
        self.tipe = tipe



class Production:
    def __init__(self):
        pass
    def purchase_material(self):
        print('Закупаем сырьё для игшрушки')

    def sewing(self):
        print('Сшиваем')

    def coloring(self):
        print('Красим')
    def add_toy(self, name, color, tipe):
        if tipe == 'plastic':
            self.purchase_material()
            self.sewing()
            self.coloring()
            toy = Plastic(name, color, tipe)

        if tipe == 'glass':
            self.purchase_material()
            toy = Glass(name, color, tipe)

        if tipe == 'tree':
            self.purchase_material()
            self.coloring()
            toy = Tree(name, color, tipe)

        return toy

pl_pengvin = Production().add_toy('biba', 'black-white', 'tree')

print(pl_pengvin.color, pl_pengvin.tipe)
print(type(pl_pengvin))
print(pl_pengvin.__class__.__name__)






# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка