class Solution:
    def reverseWords(self, s: str) -> str:
        s_words = s.split(' ')
        res = []
        for word in s_words:
            res.append(word[::-1])
        return ' '.join(res)
