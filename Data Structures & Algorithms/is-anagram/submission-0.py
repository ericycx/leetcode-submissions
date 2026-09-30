class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = {}
        for ch in s:
            if ch not in hashSet:
                hashSet[ch] = 1
            else:
                hashSet[ch] += 1
        for ch in t:
            if ch not in hashSet:
                return False
            hashSet[ch] -= 1
        for k in hashSet:
            if hashSet[k] != 0:
                return False
        return True