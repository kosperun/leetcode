class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s)) == 1 or s == s[::-1]:
            return s
        res = s[0]
        lgth = len(s)
        min_len = 1
        for i in range(lgth):
            if i + min_len >= lgth:
                return res
            for j in range(lgth, i, -1):
                if j - i <= min_len:
                    break
                else:
                    # lres = len(res)
                    sub_s = s[i:j]
                    # lsub = len(sub_s)
                    # if lsub > min_len:
                    rev_sub_s = sub_s[::-1]
                    if sub_s == rev_sub_s:
                        res = sub_s
                        min_len = len(res)
        return res