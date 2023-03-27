class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        for q in queries:
            max_len = 0
            max_sum = 0
            for _, num in enumerate(nums):
                max_sum += num
                if max_sum <= q:
                    max_len += 1
            answer.append(max_len)
        return answer
        