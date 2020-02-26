# -*- coding:utf-8 -*-
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# 和为S的两个数字
class Solution_1:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        index = 1
        result = {}
        for x in array[:-1]:
            y = tsum - x
            if y >= x:
                search_result = self.biSearch(array[index:],y)
                if search_result != -1:
                    result[x * y] = [x, y]
            index += 1
        if not result:
            return []
        min_num = min(result.keys())
        return result[min_num]

    def biSearch(self, array, k):
        start, end = 0, len(array) - 1
        while start <= end:
            mid = start + int((end - start)/2)
            if array[mid] == k:
                return mid
            elif array[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left, right = 0,len(array) - 1
        while left < right:
            if array[left] + array[right] == tsum:
                return [array[left], array[right]]
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1
        return []


s = Solution()
result = s.FindNumbersWithSum([1,2,4,7,11,15],15)
print(result)
