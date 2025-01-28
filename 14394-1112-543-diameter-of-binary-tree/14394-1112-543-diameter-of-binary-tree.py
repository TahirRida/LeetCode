# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def depth(node):
            if not node:
                return 0
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the maximum diameter
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the height of the current subtree
            return 1 + max(left_depth, right_depth)
        
        depth(root)  # Start the recursive depth calculation
        return self.max_diameter
        
        