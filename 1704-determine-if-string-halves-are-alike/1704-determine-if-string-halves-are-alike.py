class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1, s2  = s[:len(s)//2], s[len(s)//2:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return sum([1 for el in s1 if el in vowels]) == sum([1 for el in s2 if el in vowels])