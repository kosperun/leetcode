class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}
        for el in arr:
            if el in cnt:
                cnt[el] += 1
            else:
                cnt[el] = 1
        return len(set(cnt.values())) == len(set(arr))