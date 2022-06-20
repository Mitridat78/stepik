"""

Найдите первое вхождение подстроки в строку
Верните индекс первого вхождения подстроки в строку или -1, если подстрока 
не является частью строки.
Sample Input:
hello
ll
Sample Output:
2
"""
str = input()
substr = input()
print(str.find(substr))