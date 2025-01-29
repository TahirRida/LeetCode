# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])  # Initialize queue with the root node
        res = []

        while queue:
            curr_res = []
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()   # Retrieve the front node
                curr_res.append(node.val)
                
                if node.left:  # Add left child if exists
                    queue.append(node.left)
                if node.right: # Add right child if exists
                    queue.append(node.right)
            
            res.append(curr_res)  # Append level-wise results
        
        return res

        