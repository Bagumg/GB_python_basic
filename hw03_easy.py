# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    mult_num = pow(10, int(ndigits))
    multiply_float = number * mult_num
    multiply_int = int(multiply_float)
    residue = multiply_float - multiply_int
    if not (abs(residue) < 0.5):
        if multiply_int > 0:
            multiply_int += 1
        else:
            multiply_int -= 1
    return multiply_int / mult_num



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_list = list(str(ticket_number))
    if len(ticket_list) != 6:    # В условии стоит, что функция не должна ничего принтить, поэтому возвращаем False
        return False
    if int(ticket_list[0]) + int(ticket_list[1]) + int(ticket_list[2]) == int(ticket_list[3]) + int(
            ticket_list[4]) + int(ticket_list[5]):
        return True
    else:
        return False



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))