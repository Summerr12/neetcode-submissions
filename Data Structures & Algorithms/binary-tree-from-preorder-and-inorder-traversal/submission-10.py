# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder [root, left, right]
        #inorder visits left, root, then right
        #we take preorder from left to right to see which is the next root
        #we take inorder to split between

        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_index = 0 #counter for preorder

        def addingChildren(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            #remove the root value from parameters
            root.left = addingChildren(l, mid-1)
            root.right = addingChildren(mid+1, r)
            return root

        return addingChildren(0, len(inorder)-1)
            
            
