class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacked = []
        sum_points = 0
        for op in operations:
            if op == '+':
                plus_sum = stacked[-1] + stacked[-2]
                sum_points += plus_sum
                stacked.append(plus_sum)
            elif op.isnumeric() or op[0] == '-':
                sum_points += int(op)
                stacked.append(int(op))
            elif op == 'D':
                double = 2 * stacked[-1]
                sum_points += double
                stacked.append(double)
            elif op == 'C':
                sum_points -= stacked.pop()
        return sum_points