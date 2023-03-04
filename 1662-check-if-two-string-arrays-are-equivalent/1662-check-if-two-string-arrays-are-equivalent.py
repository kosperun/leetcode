class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''
        str2 = ''
        for elem in word1:
            str1 += elem
        for elem in word2:
            str2 += elem
        return str1 == str2