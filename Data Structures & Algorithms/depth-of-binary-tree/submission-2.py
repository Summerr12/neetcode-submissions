# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # to keep track of the value, we can do a +1 counter by returning 1+ func call
        if root == None: return 0 #end of a path
        
        countL = self.maxDepth(root.left) +1
        countR = self.maxDepth(root.right) +1
        
        return max(countL, countR)