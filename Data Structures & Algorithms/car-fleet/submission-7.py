class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stacked = []
        sorted_list = [(-1,-1)] * (max(position) + 1)
        for i in range(len(position)):
            sorted_list[position[i]] = (position[i], speed[i])
        for pos,spd in sorted_list:
            if pos == -1:
                pass
            else:
                hours = (target - pos) / spd
                while stacked and stacked[-1] <= hours:
                    stacked.pop()
                stacked.append(hours)
        return len(stacked)