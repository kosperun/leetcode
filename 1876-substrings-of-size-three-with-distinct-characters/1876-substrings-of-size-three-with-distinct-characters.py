class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sub_str = [s[i:i+3] for i in range(len(s)-2)]
        res = 0
        for sub in sub_str:
            if len(set(sub)) == 3:
                res += 1
        return res
