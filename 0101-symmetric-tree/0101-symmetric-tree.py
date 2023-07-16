# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def postorder(self, root, mode="left"):
        magic = -101
        if root is None:
            return [magic]
        
        result = []
        if mode == "left":
            result += self.postorder(root.left, mode)
            result += self.postorder(root.right, mode)
        else:
            result += self.postorder(root.right, mode)
            result += self.postorder(root.left, mode)        
        result += [root.val]
        return result
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        if not (root.left is not None and root.right is not None):
            return False
        
        left_subtree = self.postorder(root.left, "left")
        right_subtree = self.postorder(root.right, "right")
        
        if not len(left_subtree) == len(right_subtree):
            return False
        for i, l_e in enumerate(left_subtree):
            r_e = right_subtree[i]
            if not l_e == r_e:
                return False
        return True
        