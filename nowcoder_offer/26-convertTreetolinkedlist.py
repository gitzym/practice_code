# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree:
            head, tail = self.traverse(pRootOfTree)
            return head
        else:
            return None

    def traverse(self, root):
        if root:
            if root.left is None and root.right is None:
                return root, root
            head, tail = None, None
            l_head, l_tail = self.traverse(root.left)
            if l_tail:
                l_tail.right = root
                root.left = l_tail
                head = l_head
            else:
                head = root

            r_head, r_tail = self.traverse(root.right)
            if r_head:
                r_head.left = root
                root.right = r_head
                tail = r_tail
            else:
                tail = root

            return head, tail
        return None, None


class Solution_offical:
    def Convert(self, pRootOfTree):
        if pRootOfTree:
            self.convertHelper(pRootOfTree, None)
            while pRootOfTree.left:
                pRootOfTree = pRootOfTree.left
            return pRootOfTree
        else:
            return None

    def convertHelper(self,cur,pre):
        if cur is None:
            return
        result = self.convertHelper(cur.left, pre)

        cur.left = pre
        if pre:
            pre.right = cur
        pre = cur
        self.convertHelper(cur.right, pre)


class Solution_:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        root, pre = None, None
        isRoot = True
        cur = pRootOfTree
        stack = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            p = stack.pop()

            if isRoot:
                root = p
                pre = root
                isRoot = False
            else:
                pre.right = p
                p.left = pre
                pre = p
            cur = p.right
        return root





# s = Solution()
# s = Solution_offical()
s = Solution_()
root = TreeNode(10)
left = TreeNode(5)
right = TreeNode(15)
root.left = left
root.right = right
x = s.Convert(root)

while x:
    l = None
    r = None
    print(x.val)
    if x.left:
        l = x.left.val
    if x.right:
        r = x.right.val

    print(x,'pre:',l,'next:',r)

    x = x.right

