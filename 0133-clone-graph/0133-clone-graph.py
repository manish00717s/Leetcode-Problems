class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(node):
            # already cloned
            if node in old_to_new:
                return old_to_new[node]
            
            # create clone
            copy = Node(node.val)
            old_to_new[node] = copy
            
            # clone neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)