# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#1 递归
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot:
            return 1 + max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))
        else:
            return 0
#2 非递归，层序遍历
class Solution_:
    def TreeDepth(self, pRoot):
        # write code here
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