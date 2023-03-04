class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapp = "abcdefghij"
        return int("".join([str(mapp.index(el)) for el in firstWord])) + int(
            "".join([str(mapp.index(el)) for el in secondWord])
        ) == int("".join([str(mapp.index(el)) for el in targetWord]))

###
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapp = "abcdefghij"
        first_value = "".join([str(mapp.index(el)) for el in firstWord])
        second_value = "".join([str(mapp.index(el)) for el in secondWord])
        third_value = "".join([str(mapp.index(el)) for el in targetWord])
        return int(first_value) + int(second_value) == int(third_value)
