# 数组中只出现一次的两个数字【异或】
class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []

        temp = 0
        for i in array:
            temp = temp ^ i

        index = 0
        while (temp & 1) == 0:  # 括号加上
            temp = temp >> 1
            index +=  1

        a, b = 0, 0
        for i in array:
            if self.isBit(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self,num, index):
        num = num >> index
        return num & 1




l = [-14,-14,13,-16,13,12,15,15]
s = Solution()
x = s.FindNumsAppearOnce(l)
print(x)

print(0b1101 & 1 == 1)
