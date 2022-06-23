"""
Данн список чисел nums размером n.
Верните самый часто повторяемый элемент из списка. Часто повторяемый это элемент, 
который появляется больше чем [n/2]

Sample Input:
3,2,3

Sample Output:
3
"""
nums = [int(i) for i in input().split(',')]
a = {}
for elem in nums:
    if elem not in a:
        a[elem] = 1
    else:
        a[elem] += 1
    if a[elem] > len(nums)/2:
        print(elem)
