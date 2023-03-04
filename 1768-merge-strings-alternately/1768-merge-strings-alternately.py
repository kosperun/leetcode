class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = word1
        longer = word2
        if len(word2) < len(word1):
            shorter = word2
            longer = word1
        res = []
        for i in range(len(shorter)):
            res.extend([word1[i], word2[i]])
        res.append(longer[len(shorter):])
        return "".join(res)