class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = [0] * 26
        
        for c in s:
            cnt[ord(c)-ord("a")] += 1
            
        seen = set()
        res = 0
        cnt.sort(reverse=True)
        
        for freq in cnt:
            while freq in seen:
                res += 1
                freq -= 1
                
            if freq:
                seen.add(freq)
            
        return res