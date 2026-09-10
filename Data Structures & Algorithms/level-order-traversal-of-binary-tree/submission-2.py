# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #list

        #BFS
        q = [root] #first node

        while q: # while nodes available
            qLength = len(q) # len of curr nodes in q
            level = []
            for i in range(qLength): # for all nodes in level
                node = q.pop(0) # pop the leftmost node(smallest num)
                if node: #if it exists
                    level.append(node.val) #append it to the level list
                    q.append(node.left) #add its children to the back of the list
                    q.append(node.right)
                    #it only act on its level based off qLength
            if level: #if we have read nodes into level, move it into res as a list
                res.append(level)
        return res