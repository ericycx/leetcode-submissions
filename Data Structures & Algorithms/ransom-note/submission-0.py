class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        thing = Counter(magazine)
        for letter in ransomNote:
            if letter in thing:
                thing[letter] -= 1
                if thing[letter] == 0:
                    del thing[letter]
            else:
                return False
        return True
