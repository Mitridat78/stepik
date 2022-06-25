"""
Дана строка. Найдите первый неповторяющийся символ в этой 
строке и верните его индекс. Если такого элемента нет, то верните -1 (минус один).

Sample Input:
leetcode

Sample Output:
0
"""

s = input()
count1 = 0

for elem in s:
    if s.count(elem) == 1:
        print(s.index(elem))
        count1 += 1
        break
if count1 == 0:
    print(-1)    
        