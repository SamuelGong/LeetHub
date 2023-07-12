# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = [root]
        level_queue = [0]
        create_new_level = True
        while len(queue) > 0:
            node = queue.pop(0)
            level = level_queue.pop(0)
            if len(result) < level + 1:
                result.append([node.val])
            else:
                result[level].append(node.val)
                
            if node.left is not None:
                queue.append(node.left)
                level_queue.append(level + 1)
            if node.right is not None:
                queue.append(node.right)
                level_queue.append(level + 1)

        return result
        