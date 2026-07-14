import heapq

class Solution:
    def minimumEffortPath(self, heights):

        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        seen = set()

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in seen:
                continue
            seen.add((r, c))

            if r == m - 1 and c == n - 1:
                return effort

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    newEffort = max(
                        effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )
                    heapq.heappush(heap, (newEffort, nr, nc))