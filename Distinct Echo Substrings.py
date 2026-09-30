class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        mod1 = 1_000_000_007
        mod2 = 1_000_000_009
        base = 911382323

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, ch in enumerate(text):
            x = ord(ch) - ord('a') + 1
            pow1[i + 1] = pow1[i] * base % mod1
            pow2[i + 1] = pow2[i] * base % mod2
            pref1[i + 1] = (pref1[i] * base + x) % mod1
            pref2[i + 1] = (pref2[i] * base + x) % mod2

        def get_hash(l, r):
            h1 = (pref1[r] - pref1[l] * pow1[r - l]) % mod1
            h2 = (pref2[r] - pref2[l] * pow2[r - l]) % mod2
            return h1, h2

        seen = set()

        for length in range(2, n + 1, 2):
            half = length // 2

            for start in range(n - length + 1):
                mid = start + half
                end = start + length

                if get_hash(start, mid) == get_hash(mid, end):
                    seen.add(get_hash(start, end))

        return len(seen)
