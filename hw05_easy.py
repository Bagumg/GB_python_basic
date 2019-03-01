import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dirs():
    for i in range(1,10):
        os.mkdir(f'dir_{i}')

def del_dirs():
    for i in range(1,10):
        os.rmdir(f'dir_{i}')

# Сложнее читается генератором, на мой взгляд, поэтому через for оставил

# [os.mkdir(f'dir_{i}') for i in range(1, 9)]
# [os.rmdir(f'dir_{i}') for i in range(1, 9)]

make_dirs()
del_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    os.listdir()

list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(filename):
    if os.path.isfile(filename):
        copy = filename + '.copy'
        shutil.copy(filename, copy)
        if os.path.exists(copy):
            print("Файл ", copy, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

copy_file('hw05_easy.py')

# shutil.copy(sys.argv[0], sys.argv[0] + '_copy.py')