class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - ord('a') + 1 for c in s)
        left = 0

        for i in range(len(s) - 1):
            left += ord(s[i]) - ord('a') + 1

            if left * 2 == total:
                return True

        return False
