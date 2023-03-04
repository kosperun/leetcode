class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        inter_sum = 0
        for item in nums:
            inter_sum += item
            run_sum.append(inter_sum)
        return run_sum
            
            