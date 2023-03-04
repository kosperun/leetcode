class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for elem in sentences:
            temp = len(elem.split(" "))
            if temp > res:
                res = temp
        return res