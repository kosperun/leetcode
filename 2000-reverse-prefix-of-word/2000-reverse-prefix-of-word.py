class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        ind = word.find(ch)
        prefix = word[:ind+1]
        return prefix[::-1] + word[ind+1:]