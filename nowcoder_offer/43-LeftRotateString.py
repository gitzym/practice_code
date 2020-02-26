# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]

# YX = (XTY T)T
s = "abc"
print(s[4:]+s[:4])
# ss = reversed(s)
# print(ss,s)