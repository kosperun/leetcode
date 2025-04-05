class Solution:
    res = 0
    
    def get_subs(self, nums):
        def dfs(index, path):
            if index == len(nums):
                yield path
                return
            yield from dfs(index + 1, path + [nums[index]])
            yield from dfs(index + 1, path)
        yield from dfs(0, [])

    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0
        for sub in self.get_subs(nums):
            res = 0
            for num in sub:
                res ^= num
            xor_sum += res
        return xor_sum

        