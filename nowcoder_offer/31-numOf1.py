# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        times = 0

        for i in range(1, n+1):
            for s in str(i):
                if s == '1':
                    times += 1

        return times

    def NumberOf1(self,number):
        times = 0
        for s in str(number):
            if s == '1':
                times += 1
        return times


# s = Solution()
# x = s.NumberOf1(11111)
# print(x)

print(int(2345/10)%10)
print(int(2345/100)%100)
print(int(2345/1000)%1000)
