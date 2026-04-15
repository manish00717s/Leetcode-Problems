from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # Queue for courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses