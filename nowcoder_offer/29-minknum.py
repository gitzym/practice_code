class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        tinput.sort()
        return tinput[:k]

class Solution_heap:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        heap = self.init_heap(tinput[0:k])

        for y in tinput[k:]:
            if y < heap[0]:
                heap[0] = y
                heap = self.adjustHeap(heap)

        return sorted(heap)

    def init_heap(self,heap):
        for x in range(int((len(heap)/2)) - 1, -1,-1):
            print(x)
            heap[x:] = self.adjustHeap(heap[x:])
        return heap

    def adjustHeap(self,heap):
        print('init :',heap)
        length = len(heap)
        last_node = int(length/2) - 1

        i = 0
        while i <= last_node:
            root = i
            left = 2 * i + 1        # right = left + 1
            if left + 1 < length and heap[left + 1] > heap[left]:
                left += 1          # left: right node

            if heap[root] < heap[left]:
                heap[root], heap[left] = heap[left],heap[root]

            print(heap[root] , heap[left], heap[left] if left + 1 < length else -1)
            print('heap: ',heap)
            i += 1
        print('--adjust done--')
        return heap

class Solution_quickSort:
    def GetLeastNumbers_Solution(self, tinput, k):
        return self.quickSort(tinput)[:k]

    def quickSort(self, numbers):
        if len(numbers) <= 1:
            return numbers
        privot = numbers[0]
        left = [x for x in numbers[1:] if x <= privot]
        right = [x for x in numbers[1:] if x > privot]
        return left + [privot] + right

ll = [4,5,1,6,2,7,3,8]
# s = Solution_heap()
s = Solution_quickSort()
rr = s.GetLeastNumbers_Solution(ll,4)
print(rr)