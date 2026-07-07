from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        visited = set()
        ans = 0

        while pq:
            time, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            ans = time

            for nei, wt in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (time + wt, nei))

        return ans if len(visited) == n else -1