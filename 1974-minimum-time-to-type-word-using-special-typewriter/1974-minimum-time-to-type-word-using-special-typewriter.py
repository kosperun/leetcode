class Solution:
    def minTimeToType(self, word: str) -> int:
        letters = list(word)
        prev = ord("a")
        res = 0
        for ch in letters:
            code = ord(ch)
            diff = abs(code - prev)
            if diff > 13:
                res += 26 - diff
            else:
                res += diff
            prev = code
            res += 1
        return res
        
