# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) <= 0:
            return 0
        # dp[i] 表示以array[i]为末尾元素的连续子向量的最大和
        dp = [i for i in array]

        for i in range(1,len(array)):
            dp[i] = max(dp[i-1] + array[i], array[i])

        return max(dp)
