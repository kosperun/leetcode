class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, el in enumerate(s):
            res += abs(123 - ord(el)) * (i+1)
        return res