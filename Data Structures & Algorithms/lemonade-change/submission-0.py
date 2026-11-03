class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0
        ten_count = 0
        for bill in bills:
            if bill == 5:
                five_count += 1
            if bill == 10:
                five_count -= 1
                if five_count < 0:
                    print(1, five_count, ten_count)
                    return False
                ten_count += 1
            if bill == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count > 2:
                    five_count -= 3
                else:
                    print(2, five_count, ten_count)
                    return False
        return True