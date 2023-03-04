class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs = nums[:n]
        ys = nums[n:]
        res = []
        for i in range(n):
            res.append(xs[i])
            res.append(ys[i])
        return res