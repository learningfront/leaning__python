# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, time, shutil


def mk_dir(path):
    os.mkdir(path)


def rm_dir(path):
    os.removedirs(path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    list_dir = [i for i in os.listdir() if os.path.isdir(i)]
    print(list_dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    path_main = os.path.relpath(__file__)
    shutil.copy2(path_main, 'copy_' + path_main)


if __name__ == "__main__":
    dir_path = 'dir_'
    [mk_dir(f'{dir_path}{i}') for i in range(1, 10)]
    [rm_dir(f'{dir_path}{i}') for i in range(1, 10)]

    list_dir()
    copy_file()

