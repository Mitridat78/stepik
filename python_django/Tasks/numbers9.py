"""
Дан массив чисел nums содержащий n чисел в диапозоне от 0 до n включительно. 
Верните только то число, которое пропущенно в последовательности.

Пример:

Дан массив nums = [3,0,1]. n = 3. В массиве 3 числа в диапозоне 
от 0 до 3 включительно пропущено число 2.
"""
nums = [int(i) for i in  input().split(',')]
nums.sort()

for i in range(len(nums)-1):
    if nums[i+1] - nums[i] > 1:
        print(nums[i]+1)





