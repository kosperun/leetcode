class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed_1 = int(str(num)[::-1])
        reversed_2 = int(str(reversed_1)[::-1])
        return num == reversed_2
        