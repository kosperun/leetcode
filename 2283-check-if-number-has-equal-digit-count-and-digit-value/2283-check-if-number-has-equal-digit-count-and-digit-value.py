class Solution:
    def digitCount(self, num: str) -> bool:
        occurence = {}
        for el in num:
            if el in occurence:
                occurence[el] += 1
            else:
                occurence[el] = 1
        for i, digit in enumerate(num):
            if str(i) not in occurence:
                if digit == "0":
                    continue
                return False
            elif str(occurence[str(i)]) != digit:
                return False
        return True