"""
Дан массив чисел. Если в нем есть дубликаты, то верните True, если нет, то False.

Sample Input:
1,2,3,1

Sample Output:
True
"""
nums = [int(i) for i in input().split(',')]
a = {}
count = 0
for elem in nums:
    if elem not in a:
        a[elem] = 1
    else:
        a[elem] += 1
        count += 1
if count >= 1:
    print("True")
else:
    print("False")