# -*- coding: utf8 -*-
class Solution(object):
    def isSameTree(self, p, q):
        #边界条件判定
        if p==q==None:
            return True
        elif p is None or q is None:  
            return False
        #逻辑实现上，多次递归
        elif p.val==q.val:  
            if self.isSameTree(p.left,q.left):
                return self.isSameTree(p.right,q.right)                
       
        return False
