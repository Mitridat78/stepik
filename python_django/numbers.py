"Римские цифры в арабские"

dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
num = input()
prev = num[-1]
res = dict1[prev]
#res = 0
for elem in num[-2::-1]:
    if dict1[elem] >= dict1[prev]:
        res += dict1[elem]
    else:
        res -= dict1[elem]
    prev = elem

print(res)