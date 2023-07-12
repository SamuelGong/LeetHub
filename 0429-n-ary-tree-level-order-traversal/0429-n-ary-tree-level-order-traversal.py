"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                
            if node.children is not None:
                for child in node.children:
                    queue.append(child)
                    level_queue.append(level + 1)

        return result