class Solution:
    def isPalindrome(self, s: str) -> bool:
        alfa_num = "".join(ch for ch in s if ch.isalnum()).lower()
        return alfa_num == alfa_num[::-1]