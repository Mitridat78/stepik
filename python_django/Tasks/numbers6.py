"""
Дан массив целых чисел, который уже отсортирован в порядке возрастания, найдите два числа, 
которые складываются в целевое целевое число.

Верните индексы двух чисел таким образом (индекс начинается не с 0 как обычно, а с 1), 
чтобы числа под этими индексами суммировались в целевое значение. 
Причем индекс 1 должен быть меньше индекса 2.

Sample Input:
2,7,11,15
9

Sample Output:
[1, 2]
"""
x = [int(i) for i in  input().split(',')]
#print(x)
target = int(input())
#print(target)
count = 0

for i in range(len(x) - 1):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == target and i < j:
            print([i + 1, j + 1])
            count += 1
#    break    
if count == 0:
    print(0)    
        


