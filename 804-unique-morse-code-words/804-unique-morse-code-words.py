class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = list(map(chr, range(ord('a'), ord('z')+1)))
        morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_letters_map = dict(zip(letters, morse))
        res = set()
        for word in words:
            temp_str = ""
            for letter in word:
                temp_str += morse_letters_map[letter]
            res.add(temp_str)
        return len(res)
