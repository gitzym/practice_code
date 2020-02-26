# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        str2num = {}
        for x in list(s):
            if x in str2num.keys():
                str2num[x] += 1
            else:
                str2num[x] = 1
        i = 0
        for x in list(s):
            if str2num[x] == 1:
                return i
            i += 1
        return -1


# -*- coding:utf-8 -*-
class Solution_:
    def FirstNotRepeatingChar(self, s:str):
        # write code here
        i = 0
        for x in list(s):
            if s.count(x) == 1:
                return i
            i+=1
        return -1

s = Solution()
print(s.FirstNotRepeatingChar("google"))