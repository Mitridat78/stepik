"""
Дан отсортированный массив nums, удалите в нем дубликаты так, чтобы в результирующем массиве 
каждый элемент появлялся только один раз.
Sample Input:
1,1,2
Sample Output:
[1, 2]
"""
a = set()
nums = input().split(',')
for elem in nums:
    if elem not in a:
        a.update(elem)
print(f"[{', '.join(sorted(a))}]")

# второй способ
#print(sorted(set(map(int, input().split(',')))))
