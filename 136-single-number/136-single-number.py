class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1
        for k, v in freq.items():
            if v == 1:
                return k