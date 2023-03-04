class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(elem) for elem in str(num)]
        cnt = 0
        for elem in digits:
            if num % elem == 0:
                cnt += 1
        return cnt

