# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    #dictate Null nodes and delimiter value
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder traversal because its the easiest to track (root, left, right)
        #insert N for every Null and a ',' for the delimiter
        result = []

        def dfs(root):
            if root is None:
                result.append("N")
                return
            result.append(str(root.val))
            
            dfs(root.left)
            dfs(root.right)
            return
        
        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #read N for every null and take the string till the delimiter
        #read each value in data split in a helper function
        #as we read the data, we add the first value and remove the first value from list
        self.pre_index = 0

        values = data.split(",")

        def build():
            #dfs style in pre order traversal like the list we made.
            #pre order decides exactly on what is left and right
            val = values[self.pre_index]
            if val == 'N': # dont need a try catch cause we set the null indicator
                self.pre_index += 1
                return None

            #connect root first (part of pre order)
            root = TreeNode(int(val))
            self.pre_index += 1 

            #traverse left and then right
            root.left = build()
            root.right = build()

            return root
            
        return build()







