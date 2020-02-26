# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法1：递归
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        l = self.TreeDepth(pRoot.left)
        r = self.TreeDepth(pRoot.right)
        return abs(l - r) <= 1 and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue = [pRoot]
        depth = 0
        while queue:
            depth += 1
            child_queue = []
            for node in queue:
                if node.left:
                    child_queue.append(node.left)
                if node.right:
                    child_queue.append(node.right)
            queue = child_queue

        return depth

# 方法2
class Solution_:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        l = self.TreeDepth(pRoot.left)
        if l == -1:
            return False
        r = self.TreeDepth(pRoot.right)
        if r == -1:
            return False

        return abs(l - r) <= 1
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        if left == -1:
            return -1
        right = self.TreeDepth(pRoot.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)

l = [1,2,3,4,7]
print(l.remove(7))
print(l)