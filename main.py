#easy
# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
name = 'slava'
age = 27
status_gay = False
print(name, age, status_gay)

real_achievements = input('Введите достижения ')
print(real_achievements)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
term = int(input('Введите число '))
print(term + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
# years_old = int(input('Введите возраст '))
#
if years_old > 18:
    print('Доступ разрешён')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

#normal
# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
while True:
    numeral = int(input('Введите число от 1 до 9'))
    if numeral > 0 and numeral < 10:
        print(numeral ** 2)
        break
    else:
        print('Число не корректное')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

digit_one = int(input('Первое '))
digit_two = int(input('Второе '))
print('первое: ', digit_one, 'Второе: ', digit_two)

digit_one = digit_two - digit_one
digit_two -= digit_one
digit_one += digit_two

print('первое: ', digit_one, 'Второе: ', digit_two)


#hard
# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

health_card = {}
health_card['Имя'] = input('Введите имя ')
health_card['Фамилия'] = input('Введите фамилию ')
health_card['Возраст'] = int(input('Введите возраст'))
health_card['Вес'] = int(input('Введите вес'))

if health_card['Возраст'] < 30 and 50 < health_card['Вес'] < 120:
    print('У тебя всё отлично')
elif health_card['Возраст'] > 30 and (health_card['Вес'] < 50 or health_card['Вес'] > 120):
    print('Задумайся')
else:
    print('You dead!!')

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!