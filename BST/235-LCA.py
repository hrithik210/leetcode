class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root

        while cur :
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right #shifting curr to right sub tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left #shifting curr to left sub tree
            else:
                return cur #we found our res