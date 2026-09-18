class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7

        left = [0] * 10
        right = [0] * 10

        for ch in s:
            right[ord(ch) - 48] += 1

        left_pair = [[0] * 10 for _ in range(10)]
        right_pair = [[0] * 10 for _ in range(10)]

        seen = [0] * 10

        for ch in s:
            d = ord(ch) - 48
            right[d] -= 1

            for a in range(10):
                right_pair[a][d] += seen[a]

            seen[d] += 1

        for ch in s:
            right[ord(ch) - 48] += 1

        ans = 0

        for ch in s:
            c = ord(ch) - 48
            right[c] -= 1

            for b in range(10):
                right_pair[c][b] -= right[b]

            for a in range(10):
                for b in range(10):
                    ans += left_pair[a][b] * right_pair[b][a]

            ans %= MOD

            for a in range(10):
                left_pair[a][c] += left[a]

            left[c] += 1

        return ans
