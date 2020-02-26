# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        thresold = length / 2
        unique_num = set(numbers)

        if len(numbers) - len(unique_num) + 1 > thresold:
            numbers2times = {}
            for num in unique_num:
                numbers2times[num] = 0

            for num in numbers:
                numbers2times[num] += 1
                if numbers2times[num] > thresold:
                    return num
        return 0


class Solution_:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) <= 1:
            return 0
        compare_num = numbers[0]
        times = 1
        for x in numbers[1:]:
            if times > 0:
                if x == compare_num:
                    times +=1
                else:
                    times -= 1
            else:
                compare_num = x
                times = 1
        times = 0
        for x in numbers:
            if x == compare_num:
                times += 1
        return compare_num if times > len(numbers)/2 else 0


class Solution_quickSort:
    # 链接：https: // www.nowcoder.com / questionTerminal / e8a1b01a2df14cb2b228b30ee6a92163?f = discussion
    # 来源：牛客网

    """对列表排序，计算下标为len/2(即中间位置)的数字数量即可"""

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 对列表进行快排
        left = 0
        right = len(numbers) - 1
        stack = [right, left]
        while stack:
            low = stack.pop()
            high = stack.pop()
            if low >= high:
                continue
            less = low - 1
            mid = numbers[high]
            for i in range(low, high):
                if numbers[i] <= mid:
                    less += 1
                    numbers[less], numbers[i] = numbers[i], numbers[less]
            numbers[less + 1], numbers[high] = numbers[high], numbers[less + 1]
            stack.extend([high, less + 2, less, low])
        # 验证
        count = 0
        length = len(numbers) // 2
        for i in numbers:
            if i == numbers[length // 2]:
                count += 1
        return numbers[length // 2] if count > length / 2.0 else 0


from collections import Counter
class Solution__:
    def MoreThanHalfNum_Solution(self, numbers):
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2:
            return count[0][0]
        return 0


s = Solution__()
x = s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
print(x)