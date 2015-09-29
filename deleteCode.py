###
class Solution(object):
    def deleteNode(self, node):
        if node.next.val == node.val:
            node.next = node.next.next            
        else:
            return self.deleteNode(node.next)
