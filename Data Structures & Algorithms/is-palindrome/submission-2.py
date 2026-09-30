class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        j = n - 1
        for i in range(n//2):
            if not s[i].isalpha() and not s[i].isnumeric():
                continue
            while not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
            if s[i].upper() != s[j].upper():
                return False
            j -= 1
        return True

    
