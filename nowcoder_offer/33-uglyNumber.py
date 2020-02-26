# -*- coding:utf-8 -*-
class Solution:
    """
    题目描述: 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
    例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
    知识点： 穷举
    """
    def GetUglyNumber_Solution(self, index):
        # write code here
        i = 1
        cur_num = 1
        while i < index:
            cur_num += 1
            if self.isUglyNumber(cur_num):
                i += 1

        return cur_num

    def isUglyNumber(self,num):
        if num == 1:
            return True
        # while type(num):
        while int(num/2) * 2 == num:
            num = int(num/2)
        if num == 1:
            return True

        while int(num/3) * 3 == num:
            num = int(num/3)
        if num == 1:
            return True

        while int(num/5) * 5 == num:
            num = int(num/5)
        if num == 1:
            return True

        return False

class Solution_:
    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        res = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(1,index):
            min_num = min(res[t2] * 2, res[t3] * 3,res[t5] * 5)
            if min_num == res[t2] * 2:
                t2+=1
            if min_num == res[t3] * 3:
                t3+=1
            if min_num == res[t5] * 5:
                t5+=1
            res.append(min_num)

        return res[-1]

s = Solution_()
x = s.GetUglyNumber_Solution(7)
print(x)