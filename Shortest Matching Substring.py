class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        MOD = 10**9 + 7
        
        a, b, c = p.split('*')
        n = len(s)

        def occurrences(t):
            if not t:
                return list(range(n + 1))

            m = len(t)
            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j and t[i] != t[j]:
                    j = lps[j - 1]
                if t[i] == t[j]:
                    j += 1
                lps[i] = j

            res = []
            j = 0

            for i in range(n):
                while j and s[i] != t[j]:
                    j = lps[j - 1]
                if s[i] == t[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = lps[j - 1]

            return res

        def next_pos(pos_list):
            nxt = [n + 1] * (n + 2)
            j = len(pos_list) - 1

            for i in range(n, -1, -1):
                if j >= 0 and pos_list[j] == i:
                    nxt[i] = i
                    j -= 1
                else:
                    nxt[i] = nxt[i + 1]

            return nxt

        occ_a = occurrences(a)
        occ_b = occurrences(b)
        occ_c = occurrences(c)

        next_b = next_pos(occ_b)
        next_c = next_pos(occ_c)

        ans = n + 1

        for i in occ_a:
            end_a = i + len(a)

            if end_a > n:
                continue

            j = next_b[end_a]

            if j > n:
                continue

            end_b = j + len(b)

            if end_b > n:
                continue

            k = next_c[end_b]

            if k > n:
                continue

            ans = min(ans, k + len(c) - i)

        return -1 if ans == n + 1 else ans
