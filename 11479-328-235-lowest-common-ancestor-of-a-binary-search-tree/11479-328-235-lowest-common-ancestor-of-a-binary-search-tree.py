# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:  # Both are in the left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val:  # Both are in the right subtree
                root = root.right
            else:
                return root  # This is the LCA
        return None  # This case should never occur if p and q exist in the tree

        