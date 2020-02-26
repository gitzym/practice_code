# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) <= 0:
            return 0
        max_length = len(str(numbers[0]))

        for num in numbers[1:]:
            if len(str(num)) > max_length:
                max_length = len(str(num))

        num2index = {}
        i = 0
        for num in numbers:
            s_num = str(num)

            if len(s_num) < max_length:
                s_num += s_num[0] * (max_length-len(s_num))

            if s_num not in num2index.keys():
                num2index[s_num] = [i]
            else:
                num2index[s_num].append(i)
            i+=1

        order_numList = sorted(num2index.keys())
        result = ""
        for num in order_numList:
            index_list = num2index[num]
            for index in index_list:
                result += str(numbers[index])
        return int(result)


import functools
class Solution_:
    def PrintMinNumber(self, numbers):
        # write code here
        compare = lambda n1,n2:int(str(n1)+str(n2)) - int(str(n1)+str(n2))
        order_list = sorted(list(numbers),key=functools.cmp_to_key(compare))
        return "".join([str(i) for i in order_list])


s = Solution_()
x = s.PrintMinNumber([3,5,1,4,2])
print(x)