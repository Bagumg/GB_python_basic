# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

import re

result = re.split(r'[A-Z]+', line) # Регулярные выражения, это просто волшебство!
print(result)


"""
Решаем задачу без re.
Пробегаемся по строке со счётчиком, который считает символы в нижнем регистре,
если натыкаемся на символ в верхнем регистре, то берём срез от начала счётчика до
i элемента в строке и дорбавляем в наш список.
Очищаем генератором наш список от пустых символов, которые образовались из-за того,
что несколько букв подряд, идут в верхнем регистре.
Затем выводим список на экран.
"""

lst = []
counter = 0
for i in range(len(line)):
    if line[i].islower():
        counter += 1
    if line[i].isupper():
        lst.append(line[i - counter: i])
        counter = 0
lst = [i for i in lst if i is not ''] # Заодно и генераторы закрепим

print(lst)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

result = re.findall(r'[a-z]{2}([A-Z]{1,})[A-Z]{2}', line)
print(result)


"""
Решаем бе re
Проходим циклом по строке. Ищем последовательность из двух символов нижнего регистра.
Если выполняется условие 2 символа нижнего регистра подряд и следующий символ в верхнем регистре,
записываем его в список. Далее отсеиваем пустые значения и значения короче трёх символов.
Делаяем срез на два символа с конца, чтобы выполнить условие(два символа в верхнем регистре, справа).
Выводим получившийся списко на экран. 
"""

counter_upper = 0
counter_lower = 0
lst = []
for i in range(len(line_2)):
    if line_2[i].islower() or counter_lower >=2:
        counter_lower += 1
        if counter_lower >=2:
           if line_2[i].isupper():
                counter_upper += 1
           elif line_2[i].islower() and line_2[i - 1].isupper():
                lst.append(line_2[i-counter_upper:i])
                counter_upper = 0
                counter_lower = 0
lst = [i for i in lst if i is not '' and len(i) >= 3]
lst = [i[:-2] for i in lst]
print(lst)





# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random

#Создаём переменные.
#Счётчик и переменную, которая будет хранить максимум счётчика

counter = 0
counterMax = 0

# Открываем файл, если его ещё не существует, то создаём новый.
# Генерируем список длинной 2500 символов со случайными числами от 0 до 9
# Создаём переменную, которая будет хранить строковое значение сгенерированного списка
# Переводим список в строку, записываем в файл и закрываем его

f = open('numbers.txt', 'w', encoding='UTF8')
numbersList = [random.randint(0, 9) for i in range(2500)]
numbersStr = ''
for i in numbersList:
       numbersStr += str(i)
f.write(numbersStr)
f.close()

# Открываем файл и считываем наше число

f = open('numbers.txt', 'r', encoding='UTF8')
numbersStr = str(f.read())

# Создаём переменную, которая будет хранить повторяющиеся число
# Проходим циклом по строке, считаем количество повторов, записываем в нашу переменную.

sameNumber = []
for i in range(len(numbersStr)):
       if numbersStr[i] == numbersStr[i - 1]:
              counter += 1
              if counter > counterMax:
                  counterMax = counter
                  sameNumber.append(numbersStr[i])
                  # Тут можно сделать так:
                  # sameNumber[0] = numbersStr[i]
                  # но я хотел закрепить, для себя, генераторы списков
                  # поэтому оставляю так, а сам генератор ниже
       else:
              counter = 0

# Берём поледнее повторяющиеся число и выводим, сколько раз оно повторялось

sameNumber = [sameNumber[-1] for i in range((counterMax + 1))]

print(sameNumber)