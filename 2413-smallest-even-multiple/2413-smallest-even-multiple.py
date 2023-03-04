class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = 2
        while True:
            if res % n == 0:
                return res
            res += 2