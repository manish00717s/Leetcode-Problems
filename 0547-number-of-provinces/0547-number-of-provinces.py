class Solution:
    def findCircleNum(self, isConnected):

        n = len(isConnected)
        seen = set()

        def dfs(city):
            seen.add(city)

            for nei in range(n):
                if isConnected[city][nei] and nei not in seen:
                    dfs(nei)

        ans = 0

        for city in range(n):
            if city not in seen:
                dfs(city)
                ans += 1

        return ans