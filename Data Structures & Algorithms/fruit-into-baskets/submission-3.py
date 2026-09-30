class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2 baskets, single type of fruit
        i = 0
        j = 0
        max_fruits = 0
        first_fruit = None
        second_fruit = (-1,-1)
        while j < len(fruits):
            if not first_fruit:
                first_fruit = fruits[i]
            if fruits[j] != first_fruit and fruits[j] != second_fruit[1]:
                if second_fruit[1] == -1:
                    second_fruit = (j, fruits[j])
                else:
                    i = second_fruit[0]
                    j = second_fruit[0]
                    first_fruit = None
                    second_fruit = (-1,-1)
            print(i,j)
            max_fruits = max(max_fruits, j - i + 1)
            j += 1
        return max_fruits

                

    