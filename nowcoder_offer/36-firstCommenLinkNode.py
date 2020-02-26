
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 and pHead2:
            node_list = []
            q1 = pHead1
            while q1:
                node_list.append(q1)
                q1 = q1.next

            q2 = pHead2
            while q2:
                if q2 in node_list:
                    return q2
                else:
                    q2 = q2.next
        return None


class Solution_:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 若不存在公共结点则最后p1和p2会同时为null并返回null
        p1 = pHead1
        p2 = pHead2
        while p1 is not p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1

