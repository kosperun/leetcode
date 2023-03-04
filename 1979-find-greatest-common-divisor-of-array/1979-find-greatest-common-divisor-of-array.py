class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        denominators = []
        for n in range(1, smallest+1):
            if smallest % n == 0 and largest % n == 0:
                denominators.append(n)
        return max(denominators)
