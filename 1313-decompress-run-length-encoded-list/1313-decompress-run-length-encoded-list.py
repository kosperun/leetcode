class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            temp = [val for i in range(freq)]
            res.extend(temp)
        return res