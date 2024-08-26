class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res =[]
        if not root:
            return TreeNode(val)
        if val > root.val:
           root.right =  self.insertIntoBST(root.right ,val)
        else: root.left =  self.insertIntoBST(root.left ,val)
        
        if node.val==val:
            return node