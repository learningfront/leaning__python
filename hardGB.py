# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2 1/4
# Вывод: 1 1/3

# quation = '-1 2/3 + -1/5'

def delimetar (q):
    tr_qua = q.split()
    new_tr_qua = []
    resalt = []

    for ind,value in enumerate(tr_qua):
        if value == '+' or value == '-':
            index_operand = ind
            new_tr_qua.append(tr_qua[:index_operand])
            new_tr_qua.append(value)
            new_tr_qua.append(tr_qua[index_operand + 1:])

    for j, i in enumerate(new_tr_qua):
        if len(i) == 2:
            new_part = []

            if '-' in i[0]:
                numerator = int(i[1].split('/')[0])
                denominator = int(i[1].split('/')[1])
                new_part.append(int(i[0]) * denominator - numerator)
                new_part.append(-1 * denominator)
                new_tr_qua[j] = new_part
            else:
                numerator = int(i[1].split('/')[0])
                denominator = int(i[1].split('/')[1])
                new_part.append(int(i[0]) * denominator + numerator)
                new_part.append(denominator)
                new_tr_qua[j] = new_part
        elif not (i == '-' or i == '+'):
            new_part = []
            numerator = int(i[0].split('/')[0])
            denominator = int(i[0].split('/')[1])
            new_part.append(numerator)
            new_part.append(denominator)
            new_tr_qua[j] = new_part


    new_tr_qua[0][0] = new_tr_qua[0][0] * abs(new_tr_qua[2][1])
    new_tr_qua[2][0] = new_tr_qua[2][0] * abs(new_tr_qua[0][1])
    new_tr_qua[0][1], new_tr_qua[2][1] = new_tr_qua[0][1] * abs(new_tr_qua[2][1]), new_tr_qua[2][1] * abs(new_tr_qua[0][1])

    if new_tr_qua[1] == '-':
        resalt.append( new_tr_qua[0][0] +   (-1) *  new_tr_qua[2][0] )
        resalt.append(abs(new_tr_qua[0][1]))
    else:
        resalt.append(new_tr_qua[0][0] + new_tr_qua[2][0])
        resalt.append(abs(new_tr_qua[0][1]))
    return resalt



def reduction_fractions(f):

    fraction = delimetar(f)
    final_resalt = ''

    if abs(fraction[0]) > fraction[1]:
        if fraction[0] < 0:
            final_resalt += '-' + str(abs(fraction[0]) // fraction[1]) + ' '
            fraction[0] = abs(fraction[0]) - (fraction[1] * (abs(fraction[0]) // fraction[1]))
            final_resalt += str(fraction[0])+'/'+str(fraction[1])
        else:
            final_resalt += str(abs(fraction[0]) // fraction[1]) + ' '
            fraction[0] = abs(fraction[0]) - (fraction[1] * (abs(fraction[0]) // fraction[1]))
            final_resalt += str(fraction[0]) + '/' + str(fraction[1])

    else:
        if fraction[0] < 0:
            final_resalt += '- '
            fraction[0] = abs(fraction[0])
            final_resalt += str(fraction[0]) + '/' + str(fraction[1])
        else:
            final_resalt += str(fraction[0]) + '/' + str(fraction[1])

    print(final_resalt)



reduction_fractions('2/3 + -2 1/5')



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))