class Solution:
    def countAsterisks(self, s: str) -> int:
        if "|" not in s:
            return s.count("*")
        bars_ind = []
        res = 0
        for i, el in enumerate(s):
            if el == "|":
                bars_ind.append(i)
        res_s = s[0 : bars_ind[0]]
        for i in range(1, len(bars_ind) - 1, 2):
            res_s += s[bars_ind[i] : bars_ind[i + 1]]
        res_s += s[bars_ind[-1] :]
        return res_s.count("*")