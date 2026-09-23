class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        M1 = 1000000007
        M2 = 1000000009
        B = 911382323

        def check(k):
            if k == 0:
                return True

            p1 = pow(B, k, M1)
            p2 = pow(B, k, M2)

            common = None

            for path in paths:
                if len(path) < k:
                    return False

                h1 = 0
                h2 = 0
                cur = set()

                for i in range(k):
                    x = path[i] + 1
                    h1 = (h1 * B + x) % M1
                    h2 = (h2 * B + x) % M2

                cur.add((h1, h2))

                for i in range(k, len(path)):
                    x = path[i] + 1
                    old = path[i - k] + 1

                    h1 = (h1 * B + x - old * p1) % M1
                    h2 = (h2 * B + x - old * p2) % M2

                    cur.add((h1, h2))

                if common is None:
                    common = cur
                else:
                    common &= cur

                if not common:
                    return False

            return True

        left = 0
        right = min(len(p) for p in paths)

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
