from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        
        # -1 = uncolored
        color = [-1] * n
        
        for start in range(n):
            if color[start] != -1:
                continue
            
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    
                    elif color[nei] == color[node]:
                        return False
        
        return True