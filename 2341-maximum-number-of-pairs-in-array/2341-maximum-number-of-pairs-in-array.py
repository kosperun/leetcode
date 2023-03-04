class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Calculate frequency of each number in nums
        hash_map = {}
        for el in nums:
            if el in hash_map:
                hash_map[el] += 1
            else:
                hash_map[el] = 1
        # Count all possible pairs and add up leftovers
        answer = [0, 0]
        for k, v in hash_map.items():
            answer[0] += v // 2
            answer[1] += v % 2
        return answer

