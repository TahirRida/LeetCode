# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        return p.val == q.val and self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
           
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False
        return (root.val == subRoot.val and (self.isSameTree(root.right,subRoot.right)) and self.isSameTree(root.left,subRoot.left)) or self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        
        