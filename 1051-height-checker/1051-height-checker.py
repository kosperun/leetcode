class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        cnt = 0
        for i, h in enumerate(heights):
            if expected[i] != h:
                cnt += 1
        return cnt