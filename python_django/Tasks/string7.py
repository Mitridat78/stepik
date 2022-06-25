"""
Дана строка. Каждое отдельное слово это сегмент. Сколько сегментов в строке?

Sample Input:
Hello, my name is John

Sample Output:
5
"""
s = input().split(' ')
count = 0
zero = 0

for elem in s:
    if elem == '' or elem == ' ':
        count += 1
    else:
        zero += 1

if count == len(s):
    print(0)    
else:
    print(zero)

""" второй способ    
s = input()
print(len(s.split(' ')) if len(s) > 1 else 0)
"""
#еще один способ
#print(len(input().split()))