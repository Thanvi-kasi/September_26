class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ans = 0
        n = len(word)

        start = 0

        while start < n:
            end = start

            while end + 1 < n and abs(ord(word[end]) - ord(word[end + 1])) <= 2:
                end += 1

            for d in range(1, 27):
                length = d * k

                if length > end - start + 1:
                    break

                count = [0] * 26

                for i in range(start, start + length):
                    count[ord(word[i]) - 97] += 1

                if all(x == 0 or x == k for x in count):
                    ans += 1

                for i in range(start + length, end + 1):
                    count[ord(word[i - length]) - 97] -= 1
                    count[ord(word[i]) - 97] += 1

                    if all(x == 0 or x == k for x in count):
                        ans += 1

            start = end + 1

        return ans
