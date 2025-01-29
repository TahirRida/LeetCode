class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))  # Parent array for Union-Find
        
        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        # Union function with union by rank
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX  # Merge without considering rank

            return True
        
        # Process edges and detect the redundant one
        for u, v in edges:
            if not union(u, v):  # If union fails, it means adding this edge creates a cycle
                return [u, v]
        
        return []


        