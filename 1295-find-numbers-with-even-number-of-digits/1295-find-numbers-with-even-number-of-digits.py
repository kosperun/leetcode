class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for el in nums:
            if len(str(el)) % 2 == 0:
                cnt += 1
        return cnt