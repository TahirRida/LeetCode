# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root:TreeNode,maxsofar:int):
            if not root:
                return 0
            isgoodnode = root.val >=maxsofar
            count = 1 if isgoodnode else 0
            maxsofar = max(root.val,maxsofar)
            count += dfs(root.right,maxsofar)
            count += dfs(root.left,maxsofar)
            return count
        
        return dfs(root,root.val)

        