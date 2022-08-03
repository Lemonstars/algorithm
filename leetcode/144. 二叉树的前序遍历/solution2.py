from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        visit = [root]
        while len(visit) > 0:
            node = visit.pop()
            res.append(node.val)

            if node.right:
                visit.append(node.right)

            if node.left:
                visit.append(node.left)

        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node4
node1.right = node3
node4.left = node2

solution = Solution()
print(solution.preorderTraversal(node1))