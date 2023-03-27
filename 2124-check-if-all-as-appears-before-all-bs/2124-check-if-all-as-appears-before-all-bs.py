class Solution:
    def checkString(self, s: str) -> bool:
        b_start = s.find('b')
        if b_start == -1:
            return True
        if 'a' in s[b_start:]:
            return False
        return True
