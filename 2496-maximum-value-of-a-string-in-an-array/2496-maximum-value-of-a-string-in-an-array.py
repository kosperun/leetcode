class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_ = 0
        for el in strs:
            curr = int(el) if el.isdigit() else len(el)
            max_ = curr if curr > max_ else max_
        return max_
            
                