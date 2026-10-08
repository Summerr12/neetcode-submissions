# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #recursive solution
        # self.count = 0
        # self.result = None

        # def inorder(root):
        #     #if there is no more children or there is a result, return
        #     if root is None or self.result is not None: 
        #         return
        #     #go left first
        #     inorder(root.left)
        #     #if min found, return
        #     if self.result is not None:
        #         return
        #     #if not found, we count the current node as visited
        #     self.count += 1
        #     #if count is now kth, set val
        #     if self.count == k: 
        #         self.result = root.val
        #         return
        #     #now go right
        #     inorder(root.right)
                

        # inorder(root)
        # return self.result

        # iterative solution
        count = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right