# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def maxPath(root):
            if root is None: return 0
   
            #post order
            left = max(maxPath(root.left),0)
            right = max(maxPath(root.right),0)

            noSplitPath = max(left,right) + root.val #finding the best non split path
            splitPath = root.val + left + right
            
            self.maxSum = max(self.maxSum, noSplitPath, splitPath, root.val)
            # print(f"no split = {noSplitPath} and split sum = {root.val + left + right}")
            #only return the non-split to see if the parent could be added
            #you cannot push up a split sum because we could cause a path error during sum
            return noSplitPath 

        #first func call
        maxPath(root)
        return self.maxSum
        