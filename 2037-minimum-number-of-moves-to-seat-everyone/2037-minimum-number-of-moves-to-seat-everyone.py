class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        cnt = 0
        seats.sort()
        students.sort()
        for i in range(len(students)):
            cnt += abs(students[i] - seats[i])
        return cnt