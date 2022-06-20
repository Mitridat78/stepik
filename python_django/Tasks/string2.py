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
str = list(input().split(','))
substr = input()
index = 0
count = 0
index1 = 0
for i in range(len(str)):
    if str[i] == substr:
        index = i
        count += 1
if count == 0:
    for j in range(len(str)):
        if str[j] <= substr:
            index1 = j + 1
    print(index1)
else:
    print(index)