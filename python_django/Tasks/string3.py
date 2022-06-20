"""
Дан отсортированный список чисел и целевое число. 
Найдите индекс целевого числа, если оно есть в списке, 
а если нету, то верните индекс где бы оно должно было быть.

Sample Input:
1,3,5,6
5
Sample Output:
2
"""
# это второй способ. Первый способ описан в файле string2
str = list(input().split(','))
substr = input()

if substr in str:
    print(str.index(substr)) #получаем индекс
else:
    str.append(substr) #добавляем
    str.sort() #сортируем
    print(str.index(substr)) #получаем индекс
