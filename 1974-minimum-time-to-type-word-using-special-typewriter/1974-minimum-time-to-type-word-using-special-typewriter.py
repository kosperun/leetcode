class Solution:
    def minTimeToType(self, word: str) -> int:
        letters = list(word)
        prev = ord("a")
        res = 0
        for ch in letters:
            code = ord(ch)
            if abs(code - prev) > 13:
                res += 26 - abs(code - prev)
            else:
                res += abs(code - prev)
            prev = code
            res += 1
        return res
        