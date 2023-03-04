class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        return [True if elem + extraCandies >= maxi else False for elem in candies]