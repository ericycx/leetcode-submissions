class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_list = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        h = []
        for key in count:
            heapq.heappush(h, (count[key], key))
            if len(h) > k:
                heapq.heappop(h)
        
        for pair in h:
            output_list.append(pair[1])
        return output_list

