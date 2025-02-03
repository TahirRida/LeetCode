# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Initialize max_sum to negative infinity
        
        def dfs(node):
            if not node:
                return 0
            
            # Recur on left and right subtrees
            left_max = max(dfs(node.left), 0)   # Ignore negative paths
            right_max = max(dfs(node.right), 0) # Ignore negative paths
            
            # Compute max path through this node
            local_max = node.val + left_max + right_max
            
            # Update global max sum
            self.max_sum = max(self.max_sum, local_max)
            
            # Return max path sum considering one side only (to be used by parent)
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_sum
        