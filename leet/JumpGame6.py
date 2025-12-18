import heapq
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heappush(heap, [-nums[0],0])
        result = nums[0]
        for i in range(1,len(nums)):

            while i - heap[0][1] > k:
                heapq.heappop(heap)
            value, index = heap[0]
            result = -value + nums[i]
            heapq.heappush(heap, [-result , i])

        return result



