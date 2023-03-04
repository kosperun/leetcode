class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums1, nums2 = set(nums[:n]), set(nums[n:])
        res = None
        if len(nums1) == 1:
            res = nums1
        elif len(nums2) == 1:
            res = nums2
        else:
            res = nums1.intersection(nums2)
        return list(res)[0]
