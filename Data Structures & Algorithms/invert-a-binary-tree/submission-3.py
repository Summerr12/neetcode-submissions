# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        trav = root

        if trav.left and trav.right:
            temp = trav.left
            trav.left = trav.right
            trav.right = temp
            self.invertTree(trav.right)
            self.invertTree(trav.left)
        elif trav.left:
            #if only one child, move sides
            trav.right = trav.left
            trav.left = None
            self.invertTree(trav.right) #move to next child
        elif trav.right: 
            trav.left = trav.right
            trav.right = None
            self.invertTree(trav.left)
        
        return root
        