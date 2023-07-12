# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level_order_result = []
        if root is None:
            return 0

        queue = [root]
        level_queue = [0]
        create_new_level = True
        while True:
            node = queue.pop(0)
            level = level_queue.pop(0)
            if len(level_order_result) < level + 1:
                level_order_result.append([node])
            else:
                level_order_result[level].append(node)
                
            s = 0
            if node.left is not None:
                queue.append(node.left)
                level_queue.append(level + 1)
            else:
                s += 1
                
            if node.right is not None:
                queue.append(node.right)
                level_queue.append(level + 1)
            else:
                s += 1
                
            if s == 2:
                return level + 1 