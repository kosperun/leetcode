class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name[0] for name in sorted(zip(names, heights), key=lambda name_height: name_height[1], reverse=True)]