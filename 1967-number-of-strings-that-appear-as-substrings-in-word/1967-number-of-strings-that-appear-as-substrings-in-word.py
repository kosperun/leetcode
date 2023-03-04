class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([int(string in word) for string in patterns])
        