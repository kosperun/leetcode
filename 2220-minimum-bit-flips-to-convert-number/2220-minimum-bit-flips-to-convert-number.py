class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(goal) > len(start):
            start = "0" * (len(goal) - len(start)) + start
        if len(start) > len(goal):
            goal = "0" * (len(start) - len(goal)) + goal
        start_list = list(start)
        goal_list = list(goal)
        cnt = 0
        for i in range(len(start_list)):
            if start_list[i] != goal_list[i]:
                cnt += 1
        return cnt
