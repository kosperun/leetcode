class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i, _ in enumerate(startTime):
            if queryTime in range(startTime[i], endTime[i]+1):
                res += 1
        return res