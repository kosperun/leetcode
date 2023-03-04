import numpy as np

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        converted = np.base_repr(n, base=k)
        return sum([int(i) for i in converted])