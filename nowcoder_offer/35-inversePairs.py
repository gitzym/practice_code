# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.p = 0
    def InversePairs(self, data):
        if len(data) <= 1:
            return 0
        number = 1000000007
        order_list = self.mergeList(data)
        return self.p% number

    def mergeList(self,data):
        if len(data) <= 1:
            return data
        mid = int(len(data)/2)
        left = self.mergeList(data[:mid])
        right = self.mergeList(data[mid:])
        l = 0
        r = 0

        merge = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merge.append(left[l])
                l+=1
            else:
                merge.append(right[r])
                r += 1
                self.p += 1
        if l < len(left):
            merge += left[l:]
        if r < len(right):
            merge += right[r:]
        return merge
    # 超时了
    # def InversePairs(self, data):
    #     number = 1000000007
    #     P = 0
    #     i = 1
    #     for x in data[1:]:
    #         for y in data[i+1:]:
    #             if x > y:
    #                 P += 1
    #         i += 1
    #     return P % number


s = Solution()
l = [5,4,3,2,1]
mid = int(len(l)/2)
x = s.mergeList(l)
print(x)
