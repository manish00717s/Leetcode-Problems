from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # Queue of courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # If all courses are included → valid
        return order if len(order) == numCourses else []