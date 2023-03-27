class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_words = text.split(" ")
        cnt = 0
        for word in text_words:
            if not set(word).intersection(set(brokenLetters)):
                cnt += 1
        return cnt
