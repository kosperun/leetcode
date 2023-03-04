class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        inter_1 = set(nums1).intersection(set(nums2))
        inter_2 = set(nums2).intersection(set(nums3))
        inter_3 = set(nums1).intersection(set(nums3))
        return inter_1 | inter_2 | inter_3