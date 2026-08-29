# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check if tree is same
        if not p and not q: return True #if both non existent
        if not p or not q: 
            print(f"false, at least one is not the same {p}  {q}")
            return False
        if p.val != q.val: 
            return False
        print(f"found for {p.val} and {q.val}")
        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check the struct of the subroot,
        # start by finding the root that equates
        if not root: return False # if no more root but subroot exists, reutrn False

        if self.isSametree(root, subRoot):
            #we may find subroot here
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        """
        root=[1,2,3,4,5]
        subRoot=[2,4,5]

        s s
        1, 2, not equal, go down root 
            2 2 equal, go down root and subRoot
                4 4 go down root and subroot
                5 5 go down root and subroot
                    None None return True
                    None None return True
            3 3 not equal, go down root
                None, 2, cause root = None, return False


        """
        