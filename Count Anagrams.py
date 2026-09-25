class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        
        words = s.split()
        max_len = max(map(len, words))
        
        fact = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], MOD - 2, MOD)
        
        for i in range(max_len, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        
        ans = 1
        
        for word in words:
            freq = [0] * 26
            
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            ways = fact[len(word)]
            
            for count in freq:
                ways = ways * inv_fact[count] % MOD
            
            ans = ans * ways % MOD
        
        return ans
