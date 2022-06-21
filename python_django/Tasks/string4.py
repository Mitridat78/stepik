"""
Дана строка s состоящая из нескольких слов, разделенных пробелами,
верните длину последнего слова в строке. Если последнее слово не 
существует, верните 0.

Sample Input:
Hello World
Sample Output:
5
"""
# 
s = input()
if len(s) == 0:
    print(0)
else:
    print(len(s[s.rfind(' ')+1:]))

# второй способ
#s = input().split(' ')
#print(len(s[-1]))

""" третий способ
s = input()
print(0 if len(s)==0 else len(s[s.rfind(' ')+1:]))
"""