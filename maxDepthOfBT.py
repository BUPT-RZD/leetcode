# -*- coding: utf-8 -*-

#DFS
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            #递归，记得self调用
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1



#BFS 关键点是队列

    
