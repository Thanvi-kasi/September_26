class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        order = [0]

        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n)]

        for u in reversed(order):
            for parity in range(2):
                for dist in range(k + 1):
                    sign = -1 if parity else 1

                    total = sign * nums[u]

                    for v in g[u]:
                        if parent[v] == u:
                            total += dp[v][parity][min(dist + 1, k)]

                    dp[u][parity][dist] = total

                    if dist >= k:
                        total = -sign * nums[u]

                        for v in g[u]:
                            if parent[v] == u:
                                total += dp[v][1 - parity][1]

                        dp[u][parity][dist] = max(
                            dp[u][parity][dist],
                            total
                        )

        return dp[0][0][k]
