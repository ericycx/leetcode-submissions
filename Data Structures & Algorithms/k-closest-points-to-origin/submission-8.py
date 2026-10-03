class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for point in points:
            dist = -1 * (point[0] ** 2 + point[1] ** 2)
            if len(res) < k:
                heapq.heappush(res, [dist, point[0], point[1]])
            else:
                if dist > res[0][0]:
                    heapq.heappop(res)
                    heapq.heappush(res, [dist, point[0], point[1]])
        return [[x,y] for _,x, y in res]
                

