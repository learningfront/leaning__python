# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# class TownCar:
#     def __init__(self, name, speed, color, is_police = False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#
#     def go(self):
#         print('Машина поехала!')
#
#     def stop(self):
#         print('Машина остановилась!')
#
#     def turn(self, direction):
#         print(f'Машина повернула {direction}!')
#
#
# my_car = TownCar('bmw', 120, 'red', True)
#
# print(my_car.is_police)
# my_car.turn('направо')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, name, color, max_speed = 60):
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула {direction}!')


class TownCar(Car):
    def location(self):
        print('Машина находится в Москве')

class SportCar(Car):
    def upp_grade(self):
        print('Машину можно ещё улучшить')

class PoliceCar(Car):
    def __init__(self, name, color, is_police, max_speed = 60):
        super().__init__(name, color, max_speed)
        self.is_police = is_police


my_car = TownCar('bmw', 'red')
my_sport_car = SportCar('ferrari', 'black', 150)
my_police_car = PoliceCar('ford',  'blue', True, 100)

print(my_police_car.is_police)