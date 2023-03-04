class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1
        for k, v in freq.items():
            if v > int(len(nums) / 2):
                return k