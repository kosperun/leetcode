class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0 for elem in s]
        for i in range(len(s)):
            res[indices[i]] = s[i]
        res = ''.join(res)
        return res