# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers:list):
        # write code here
        numbers.sort()
        print(numbers)
        count_zero = 0
        for i in range(len(numbers)-1):
            if numbers[i] == 0:
                count_zero +=1
            else:
                diff = numbers[i+1] - numbers[i]
                if diff > 1:
                    count_zero -= (diff - 1)
                    if count_zero < 0:
                        return False
                if diff < 1:
                    return False
        return True

'''
用数组d来判断是否有除了0以外的重复数，max记录最大值，min记录最小值，再判断是否差<5
max 记录 最大值, 初始化为-1
min 记录  最小值， 初始化为14
min ,max 都不记0
满足条件 1 max - min <5
         2 除0外没有重复的数字(牌)
        3 数组长度 为5
'''

s = Solution()
res = s.IsContinuous([0,3,2,6,4])
print(res)