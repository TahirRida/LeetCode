# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # Store inorder indices in hashmap
        
        def helper(pre_start, in_start, in_end):
            if pre_start >= len(preorder) or in_start > in_end:
                return None
            
            # Get the root value and create the node
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the index of root in inorder (O(1) lookup)
            root_index = inorder_map[root_val]

            # Number of nodes in the left subtree
            left_size = root_index - in_start
            
            # Recursively construct left and right subtrees
            root.left = helper(pre_start + 1, in_start, root_index - 1)
            root.right = helper(pre_start + left_size + 1, root_index + 1, in_end)

            return root

        return helper(0, 0, len(inorder) - 1)

        