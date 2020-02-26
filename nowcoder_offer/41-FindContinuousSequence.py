# -*- coding:utf-8 -*-
# 和为S的连续正数序列
class Solution:
    def FindContinuousSequence(self, tsum):
        n = int((2 * tsum) ** 0.5)

        result = []
        # tsum = start * n + (n ** 2 -n )/2
        while n >= 2:
            c = tsum - (n * (n - 1)) / 2
            if c % n == 0:
                start = int(c/n)
                result.append(list(range(start, start + n)))
            n -= 1

        return result

s = Solution()
r = s.FindContinuousSequence(6)
print(r)
for x in r:
    print(sum(x))

