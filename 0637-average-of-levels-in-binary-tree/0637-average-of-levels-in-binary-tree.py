# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_order_result = []
        result = []
        if root is None:
            return result

        queue = [root]
        level_queue = [0]
        create_new_level = True
        while len(queue) > 0:
            node = queue.pop(0)
            level = level_queue.pop(0)
            if len(level_order_result) < level + 1:
                level_order_result.append([node.val])
            else:
                level_order_result[level].append(node.val)
                
            if node.left is not None:
                queue.append(node.left)
                level_queue.append(level + 1)
            if node.right is not None:
                queue.append(node.right)
                level_queue.append(level + 1)

        for level in level_order_result:
            result.append(sum(level) / len(level))
        return result