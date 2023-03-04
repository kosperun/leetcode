class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_ = 0
        for j in range(1, len(arr) + 1, 2):
            for i in range(len(arr)):
                if j + i <= len(arr):
                    sum_ += sum(arr[i : i + j])
        return sum_