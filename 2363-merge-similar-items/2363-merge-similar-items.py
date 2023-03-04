class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = {}
        for el in items1:
            if el[0] in items:
                items[el[0]] += el[1]
            else:
                items[el[0]] = el[1]
        for el in items2:
            if el[0] in items:
                items[el[0]] += el[1]
            else:
                items[el[0]] = el[1]
        res = [[key, value] for key, value in items.items()]
        return sorted(res)