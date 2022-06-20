"""Дано 32-битное целое число x, верните x развернув в 
обратную сторону. Если реверсирование x приводит к выходу значения 
за пределы 32-битного целочисленного диапазона со знаком [-231, 231-1], 
то верните 0.Ограничения: -231 <= x <= 231-1
"""
# Решение через функцию
def razvorot(old_num):

    if int(old_num) > 0:
        new_num = old_num[::-1] # разворачиваем список в обратном порядке
        if (-2)**31 <= int(new_num) <= (2**31) - 1:
            return int(new_num)
        else:
            return 0
    elif int(old_num) == 0:
        return 0
    else: #если меньше 0
        new_num = 0
        new_num = old_num[len(old_num)-1:0:-1] # разворачиваем список в обратном порядке и отбрасываем знак минус
        new_num=int(new_num)*(-1) # возвращаем знак минус числу
        if (-2)**31 <= int(new_num) <= (2**31) - 1:
            return int(new_num)
        else:
            return 0

old_num = input()
print(razvorot(old_num))