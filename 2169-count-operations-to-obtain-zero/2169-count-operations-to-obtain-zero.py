class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        small, big = (num1, num2) if num1 <= num2 else (num2, num1)
        cnt = 0
        while small > 0 and big > 0:
            big -= small
            small, big = (small, big) if small <= big else (big, small)
            cnt += 1
        return cnt