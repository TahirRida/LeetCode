# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        que = deque([root])
        
        while que:
            level_size = len(que)
            for i in range(level_size):
                curr = que.popleft()
                if i == level_size - 1:  # Only add the rightmost node of the level
                    res.append(curr.val)
                
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

        return res