# -*- coding: utf-8 -*-
#bsa 左比root小，右比root大
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if max(p.val,q.val)<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val)>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
       
