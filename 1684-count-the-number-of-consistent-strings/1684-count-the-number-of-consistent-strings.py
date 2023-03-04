class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        cnt = 0
        for word in words:
            if set(word).issubset(allowed_set):
                cnt += 1
        return cnt

        