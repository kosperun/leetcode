class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = {}
        for el in s:
            if el not in res:
                res[el] = s.index(el)
            else:
                return el
