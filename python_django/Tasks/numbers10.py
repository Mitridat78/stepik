"""
Дан целочисленный массив nums, найдите три числа, произведение которых
является максимальным, и верните максимальное произведение.

Sample Input:
1,2,3

Sample Output:
6
"""
nums = [int(i) for i in input().split(',')]
proiz = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k and nums[i] * nums[j] * nums[k] > proiz: 
                proiz = nums[i] * nums[j] * nums[k]
            elif i != j and i != k and j != k and nums[i] * nums[j] * nums[k] < proiz: 
                proiz = nums[i] * nums[j] * nums[k]
print(proiz)

""" еще один вариант
nums = [int(i) for i in  input().split(',')]
nums.sort() #сначала сортируем, в результате 3 последних числа будут максимальными
print(nums[-1]*nums[-2]*nums[-3]) #потом просто перемножием их
"""






