# 1
class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

# 2
class Solution_:
    def GetNumberOfK(self, data, k):
        index = self.biSearch(data,k)
        if index == -1:
            return 0
        else:
            pre, next = index - 1, index +1
            while pre >= 0:
                if data[pre] != k:
                    break
                pre -=1
            while next < len(data):
                if data[next] != k:
                    break
                next +=1
            return next - pre - 1

    def biSearch(self,data,k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + int((end - start)/2)
            if data[mid] == k:
                return mid
            elif data[mid] > k:
                end  = mid - 1
            else:
                start = mid + 1
        return start

# 3
class Solution_bSearch:
    def GetNumberOfK(self, data, k):
        first = self.biSearch_first(data,k)
        if first == -1:
            return 0
        else:
            return self.biSearch_last(data,k) - first + 1

    def biSearch_last(self,data,k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + int((end - start)/2)
            if data[mid] == k:
                if mid + 1 >= len(data) or data[mid+1] !=k:
                    return mid
                else:
                    start = mid + 1
            elif data[mid] > k:
                end  = mid - 1
            else:
                start = mid + 1
        return -1

    def biSearch_first(self,data,k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + int((end - start)/2)
            if data[mid] == k:
                if mid - 1 < 0 or data[mid-1] !=k:
                    return mid
                else:
                    end = mid - 1
            elif data[mid] > k:
                end  = mid - 1
            else:
                start = mid + 1
        return -1

# 4
class Solution_bSearch_:
    def GetNumberOfK(self, data, k):
        return self.biSearch(data,k-0.5) - self.biSearch(data, k+0.5)

    def biSearch(self,data,k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + int((end - start)/2)
            if data[mid] > k:
                end  = mid - 1
            else:
                start = mid + 1
        return start


# l = [1,2,3,4,5,1,2,3,4]
# print(l.count(1))

s = Solution_()
print(s.GetNumberOfK([1,2,3,3,3,3,4,5],3))


# for i in range(0,10,-1):
#     print(i)

