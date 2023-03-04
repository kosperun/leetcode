class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        arr.extend([0 for i in encoded])
        for i in range(1, len(arr)):
            arr[i] = encoded[i-1] ^ arr[i-1]
        return arr
