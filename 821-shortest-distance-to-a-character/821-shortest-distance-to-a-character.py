class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        c_indexes = sorted([i for i, el in enumerate(s) if el == c])
        closest_ind = 0
        for i, el in enumerate(s):
            # if el == c:
            #     answer.append(0)
            # else:
            if (closest_ind < len(c_indexes) - 1) and abs(i - c_indexes[closest_ind]) > abs(i - c_indexes[closest_ind + 1]):
                closest_ind += 1
            answer.append(abs(i - c_indexes[closest_ind]))
        return answer