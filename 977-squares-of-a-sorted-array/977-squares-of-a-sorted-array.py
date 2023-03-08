class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [item**2 for item in sorted(nums, key=lambda x: abs(x))]
        
        