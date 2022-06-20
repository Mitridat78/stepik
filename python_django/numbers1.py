"""Дано 32-битное целое число x, верните x развернув в 
обратную сторону. Если реверсирование x приводит к выходу значения 
за пределы 32-битного целочисленного диапазона со знаком [-231, 231-1], 
то верните 0.Ограничения: -231 <= x <= 231-1
"""
"""old_num = int(input())
new_num = 0

while old_num % 10 > 0:
#    if old_num % 10 > 0:
    new_num += old_num % 10
    old_num = old_num // 10
    new_num *= 10
    
if (-2)**31 <= new_num <= (2**31) - 1:
    print(new_num)
else:
    print(0)
    """


old_num = input()

if int(old_num) > 0:
    new_num = old_num[::-1]
    if (-2)**31 <= int(new_num) <= (2**31) - 1:
        print(int(new_num))
    else:
        print(0)
elif int(old_num) == 0:
    print(0)
else:
    new_num = 0
    new_num = old_num[len(old_num)-1:0:-1]
    new_num=int(new_num)*(-1)
    if (-2)**31 <= int(new_num) <= (2**31) - 1:
        print(int(new_num))
    else:
        print(0)
