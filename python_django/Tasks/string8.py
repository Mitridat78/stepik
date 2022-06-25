"""
Дана строка, проверьте, может ли она состоять из повторяющихся подстрок.

Sample Input:
abab

Sample Output:
True
"""
s = input()
s1, s2 = s[0:len(s)//2], s[len(s)//2:]
if s1 == s2:
    print("True")
else:
    print("False")
