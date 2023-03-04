class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for el in words:
            if el == el[::-1]:
                return el
        return ""
