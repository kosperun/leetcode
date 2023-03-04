class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        ind = {elem[-1]: elem[:-1] for elem in s_list}
        res = ""
        for key in sorted(ind.keys()):
            res += ind[key] + " "
        return res.strip()
        