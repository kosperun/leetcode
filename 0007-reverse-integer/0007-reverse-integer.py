class Solution:
    def reverse(self, x: int) -> int:
        # if x < 0:
        #     x = str(x)[1:]
        #     x = -int(x[::-1])
        # else:
        #     x = str(x)
        #     x = int(x[::-1])
        
        # if 2**31-1 <= x or x <= -(2**31):
        #     return 0
        # return x
        y = abs(x)
        res = []
        
        while True:
            res.append(y % 10)
            y //= 10
            if y == 0:
                break
        
        res = res[::-1]
        result = 0
        for i, dig in enumerate(res):
            result += dig * 10 ** i

        if 2**31 - 1 <= result or result <= -(2**31):
            return 0
        return result if x > 0 else -result