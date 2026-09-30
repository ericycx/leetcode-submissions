class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stacked = []
        pairs = sorted(zip(position, speed))
        for pos,spd in pairs:
            if pos == -1:
                pass
            else:
                hours = (target - pos) / spd
                while stacked and stacked[-1] <= hours:
                    stacked.pop()
                stacked.append(hours)
        return len(stacked)