class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_list = s.split(" ")
        trunc_str = " ".join(s_list[:k])
        return trunc_str.strip()