"""
Самая Длинная Непрерывная Возрастающая Подпоследовательность
Дан несортированный массив целых чисел nums, верните длину самой длинной 
непрерывной возрастающей подпоследовательности (т. е. подмассива). 
Подпоследовательность должна быть строго возрастающей.

Например:
[1, 3, 5, 4, 7] - 1, 3, 5 - это возрастающая последовательность, 
но потом идет 4. 4 меньше 5, а это значит, что последовательность прерывается. Правильный ответ 3.

Sample Input:
1,3,5,4,7

Sample Output:
3
"""

try:
    count = 0
    nums = [int(i) for i in input().split(',')]
#nums.sort()
    
    for i in range(len(nums)-1):
        if nums[i+1]>nums[i]:
            count += 1
        else:
            break
    print(count+1)
except:
    print(count)