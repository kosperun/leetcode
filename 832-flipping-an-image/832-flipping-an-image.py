class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[(i-1)%2 for i in elem] for elem in [item[::-1] for item in image]]