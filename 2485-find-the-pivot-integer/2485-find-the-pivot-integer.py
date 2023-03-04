class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n 
        for x in range(1, n):
            if sum(range(1, x+1)) == sum(range(x, n+1)):
                return x
        return -1