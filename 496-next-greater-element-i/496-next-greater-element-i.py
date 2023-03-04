class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for el in nums1:
            cur_ind = nums2.index(el)
            for item in nums2[cur_ind + 1 :]:
                if item > el:
                    res.append(item)
                    break
            else:
                res.append(-1)
        return res
