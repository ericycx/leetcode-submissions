class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacked = []
        for op in operations:
            print(stacked)
            if op == '+':
                stacked.append(stacked[-1] + stacked[-2])
            elif op.isnumeric() or op[0] == '-':
                stacked.append(int(op))
            elif op == 'D':
                stacked.append(2 * stacked[-1])
            elif op == 'C':
                stacked.pop()
        return sum(stacked)