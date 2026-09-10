# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 3 if conditions and recursive traversal
        if root == None: return None
        
        root.left, root.right = root.right, root.left #this one line cuts down 15 lines of 3 conditionals

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
        