class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1_d = {el[0]: el[1] for el in nums1}
        nums2_d = {el[0]: el[1] for el in nums2}
        res = nums1_d | nums2_d
        for key in res:
            if key in nums1_d and key in nums2_d:
                res[key] = nums1_d[key] + nums2_d[key]
        res_d = {key: res[key] for key in sorted(res)}
        return [[key, value] for key, value in res_d.items()]
