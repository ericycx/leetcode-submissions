class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                term2 = stack.pop()
                term1 = stack.pop()
                if token == '+':
                    total = term1 + term2
                elif token == '-':
                    total = term1 - term2
                elif token == '*':
                    total = term1 * term2
                else:
                    total = int(term1/term2)
                stack.append(total)
        return stack.pop()
