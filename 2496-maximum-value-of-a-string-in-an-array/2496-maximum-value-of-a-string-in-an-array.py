class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_ = 0
        for el in strs:
            if el.isdigit():
                curr = int(el)
            else:
                curr = len(el)
            if curr > max_:
                max_ = curr
        return max_
            
                