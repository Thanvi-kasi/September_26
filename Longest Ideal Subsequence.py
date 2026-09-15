class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        ans = 0

        for ch in s:
            x = ord(ch) - ord('a')

            best = 0

            for y in range(max(0, x - k), min(25, x + k) + 1):
                best = max(best, dp[y])

            dp[x] = best + 1
            ans = max(ans, dp[x])

        return ans
