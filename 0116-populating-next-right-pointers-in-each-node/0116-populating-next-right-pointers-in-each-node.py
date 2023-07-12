"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_order_result = []
        if root is None:
            return root

        queue = [root]
        level_queue = [0]
        create_new_level = True
        while len(queue) > 0:
            node = queue.pop(0)
            level = level_queue.pop(0)
            if len(level_order_result) < level + 1:
                level_order_result.append([node])
            else:
                level_order_result[level].append(node)

            if node.left is not None:
                queue.append(node.left)
                level_queue.append(level + 1)
            if node.right is not None:
                queue.append(node.right)
                level_queue.append(level + 1)

        for level in level_order_result:
            if len(level) > 1:
                for idx, e in enumerate(level[:-1]):
                    e.next = level[idx + 1]
        return root