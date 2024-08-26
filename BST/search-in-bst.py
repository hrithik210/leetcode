class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            # If the node's value matches the target value, return this node
            if node.val == val:
                return node
            
            # If val is less than the node's value, search in the left subtree
            if val < node.val:
                return dfs(node.left)
            # If val is greater than the node's value, search in the right subtree
            else:
                return dfs(node.right)
        
        # Start DFS from the root
        return dfs(root)