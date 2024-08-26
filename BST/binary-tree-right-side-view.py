class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            RightSide  = None

            for i in range(qlen):
                node = q.popleft()

                if node:
                    RightSide = node
                    q.append(node.left)
                    q.append(node.right)
                if RightSide:
                    res.append(RightSide)
            return res
