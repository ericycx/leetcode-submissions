class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sets = set()
        for first, second in paths:
            sets.add(first)
        for first, second in paths:
            if second not in sets:
                return second
        return ''