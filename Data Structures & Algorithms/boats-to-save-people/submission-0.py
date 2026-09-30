class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        list_sorted = sorted(people)
        i = 0
        j = len(people) - 1
        boats = 0
        while i <= j:
            if list_sorted[i] + list_sorted[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            boats += 1
        return boats