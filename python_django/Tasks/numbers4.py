"""
Соедините два отсортированных списка

Объедините два отсортированных связанных списка и верните его в виде отсортированного списка. 
Список должен быть составлен путем сращивания узлов первых двух списков.

Sample Input:

1,2,4
1,3,4
Sample Output:
[1, 1, 2, 3, 4, 4]
"""
x = input().split(',')
y = input().split(',')
print(sorted([int(i) for i in x if i.isdigit()] + [int(i) for i in y if i.isdigit()]))

# второй вариант
#print(sorted([int(i) for i in input().split(',') if i.isdigit()] + [int(i) for i in input().split(',') if i.isdigit()]))

""" третий вариант
x = input().split(',')
y = input().split(',')
x1 = []
y1 = []
for i in range(len(x)):
    if x[i].isdigit():
        x1.append(x[i])
for j in range(len(y)):
    if y[j].isdigit():
        y1.append(y[j])
print(f"[{', '.join(sorted(x1+y1))}]")
"""

