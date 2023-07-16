# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        levelorder_result = []
        sentinel = -101
        
        queue = [root]
        level_queue = [0]
        while len(queue) > 0:
            node = queue.pop(0)
            level = level_queue.pop(0)
            
            if len(levelorder_result) < level + 1:
                if node is not None:
                    levelorder_result.append([node.val])
                else:
                    levelorder_result.append([sentinel])
            else:
                if node is not None:
                    levelorder_result[-1].append(node.val)
                else:
                    levelorder_result[-1].append(sentinel)

            if node is not None:
                if node.left is not None:
                    queue.append(node.left)
                else:
                    queue.append(None)
                level_queue.append(level + 1)

                if node.right is not None:
                    queue.append(node.right)
                else:
                    queue.append(None)
                level_queue.append(level + 1)
                    
        if len(levelorder_result) == 2:
            return True  # only root node
            
        # at least two levels
        for level in levelorder_result[1:]:
            b, e = 0, len(level ) - 1
            while b < e:
                if not level[b] == level[e]:
                    return False
                b += 1
                e -= 1
        return True
