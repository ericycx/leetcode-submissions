class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        cur = strs[0]
        for string in strs:
            if cur != string[:n]:
                temp = ''
                i = 0
                while i < len(cur) and i < len(string) and cur[i] == string[i]:
                    temp += cur[i]
                    i += 1
                cur = temp
        return cur
                    
                    
                    