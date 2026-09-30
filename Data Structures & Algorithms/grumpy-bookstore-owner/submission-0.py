class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_sat = 0
        max_technique = 0
        local_technique = 0
        i = 0
        j = 0
        while j < len(customers):
            if j - i >= minutes:
                if grumpy[i] == 1:
                    local_technique -= customers[i]
                i += 1
            if grumpy[j] == 1:
                local_technique += customers[j]
            else:
                total_sat += customers[j]
            max_technique = max(max_technique,local_technique)
            j += 1
        print(total_sat, max_technique)
        return total_sat + max_technique
    

        
