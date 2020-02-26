# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        cur_node = pHead
        while cur_node:
            copy_node = RandomListNode(cur_node.label)
            copy_node.next = cur_node.next
            cur_node.next = copy_node
            cur_node = copy_node.next

        cur_node = pHead
        while cur_node:
            if cur_node.random:
                cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next

        new_head = pHead.next
        cur_node = pHead
        while cur_node:
            next_node = cur_node.next.next
            copy_node = cur_node.next
            cur_node.next = next_node
            if next_node:
                copy_node.next = next_node.next
            else:
                copy_node.next = None
            cur_node = next_node
        return new_head
import random
# {10,5,12,4,7},22
vl = [10,5,12,4,7]
node_list = []
for v in vl:
    node_list.append(RandomListNode(v))
i = 0
while i < len(node_list)-1:
    node_list[i].next = node_list[i+1]
    random_index =  random.randint(0,len(node_list)-1)
    if random_index == i:
        random_index = i + 1 if i<len(node_list)-1 else i-1
    node_list[i].random = node_list[random_index]
    i+=1


s = Solution()
rnode = RandomListNode(1)
p = node_list[0]
while p:
    print(p, p.label)
    if p.random:
        print(p.random.label)
    p = p.next
print('---------')
node = s.Clone(node_list[0])

while node:
    print(node, node.label)
    if node.random:
        print(node.random.label)
    node = node.next