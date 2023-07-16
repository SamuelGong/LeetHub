# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def leftmost_depth(self, root):
        node = root
        level = 0
        while node is not None:
            level += 1
            if node.left is not None:
                node = node.left
            else:
                node = None
        return level

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        s = 1
        node = root
        while True:
            if node.right is None:
                if node.left is not None:
                    return 2 * s
                else:
                    return s
            else:
                ld = self.leftmost_depth(node.left)
                rd = self.leftmost_depth(node.right)
                if ld == rd:
                    s = 2 * s + 1
                    node = node.right
                else:
                    s = 2 * s
                    node = node.left
            