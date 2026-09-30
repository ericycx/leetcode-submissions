class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0 or s[0] not in '({[':
            return False
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if stack != []:
                    compare = stack.pop()
                else:
                    return False
                if compare == '(' and s[i] != ')':
                    return False
                elif compare == '{' and s[i] != '}':
                    return False
                elif compare == '[' and s[i] != ']':
                    return False                                        
        return True if stack == [] else False