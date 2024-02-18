# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    row_fib  = [0, 1]
    for i in range(2, m):
        row_fib.append( row_fib[i-1] + row_fib[i-2])

    print(row_fib[n-1:m])

fibonacci(5,10)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    for i in range(len(origin_list) -1):
        for j in range(len(origin_list) - i - 1):
            if origin_list[j] < origin_list [j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]

    print(origin_list)



sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

def sort_to_min(list):
    resalt = []

    for x in range(len(list)):
        resalt.append(min(list))
        list.remove(min(list))

    print(resalt)




sort_to_min([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.



def my_filter(fun, elemen):
    resalt = []
    for i in elemen:
        if fun(i):
            resalt.append(i)
    return resalt

def positv_num(num):
    if num > 0:
        return True


print( my_filter(positv_num, [1, -2, 3 , -4, 5, -6]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parelelogram(dot1, dot2, dot3, dot4):
    if dot2[1] - dot3[1] == 0 and dot1[1] - dot4[1] == 0 and (dot3[0] - dot2[0] == dot4[0] - dot1[0]):
        return True


print(is_parelelogram((1, 2), (3, 4), (5, 6), (7, 8)))