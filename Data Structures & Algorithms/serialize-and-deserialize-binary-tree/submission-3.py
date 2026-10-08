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
        # if data is None: return []

        values = data.split(",")

        def build():
            #dfs style in pre order traversal like the list we made.
            val = values[self.pre_index]
            if val == 'N': # if valid num
                self.pre_index += 1
                return None

            #connect root first
            root = TreeNode(int(val))
            self.pre_index += 1 

            #traverse left and then right
            root.left = build()
            root.right = build()

            #then do stuff
            #decide which node on left or right
            return root
            
        # root = float(values[0]) #dont make the root here
        return build()







