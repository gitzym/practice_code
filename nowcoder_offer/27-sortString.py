# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        # write code here
        str_list = list(ss)
        str_list.sort()

        return self.dictOrder(str_list)


    def dictOrder(self,str_list):
        if len(str_list) <=1:
            return str_list

        order_list = []
        first_str_list= []
        for i in range(len(str_list)):
            first_str = str_list[i]
            if first_str not in first_str_list:
                first_str_list.append(first_str)
                result = self.dictOrder(str_list[:i]+str_list[i+1:])
                if type(result).__name__ == 'str':
                    order_list.append(first_str+result)
                else:
                    for s in result:
                        order_list.append(first_str+s)
        return order_list




s = Solution()
y = s.Permutation('aa')
# x = s.dictOrder(['a','b','c'])
# print(x)
print(y)