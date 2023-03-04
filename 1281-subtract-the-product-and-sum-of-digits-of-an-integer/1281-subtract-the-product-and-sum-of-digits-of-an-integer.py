class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        digits = [x for x in n_str]
        prod = 1
        for elem in digits:
            prod *= int(elem)
        sum_ = sum([int(x) for x in digits])
        return prod - sum_