# -*- coding: utf-8 -*-
#递归
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        temp=self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right=temp
        return root
#非递归
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        stack = [root]  
        while stack:  
            node = stack.pop()  
            if node:  
                node.left, node.right = node.right, node.left  
                stack += node.left, node.right  
        return root  
