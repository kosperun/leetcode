class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        res = {i: s.count(i) for i in s}
        fin = {i for i in res.values()}
        return len(fin) == 1
        
