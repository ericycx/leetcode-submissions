class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalpha() or ch == '[' or ch.isnumeric():
                stack.append(ch)
            else:
                local_string = ''
                while stack[-1] != '[':
                    local_string = stack.pop() + local_string
                stack.pop()
                i = 0
                multiplier = 0
                print(stack)
                while stack and stack[-1].isnumeric():
                    print(i)
                    multiplier += int(stack.pop()) * (10 ** i)
                    i += 1
                print(multiplier)
                stack.append(local_string * multiplier)
        return ''.join(stack)

