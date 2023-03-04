class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapp = "abcdefghij"
        return int("".join([str(mapp.index(el)) for el in firstWord])) + int(
            "".join([str(mapp.index(el)) for el in secondWord])
        ) == int("".join([str(mapp.index(el)) for el in targetWord]))
