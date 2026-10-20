class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        reach = [[False]*n for _ in range(n)]
        for u, v in prerequisites:
            reach[u][v] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = True
        return [reach[u][v] for u, v in queries]
