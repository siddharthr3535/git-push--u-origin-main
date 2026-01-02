import heapq
from typing import Counter, List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = []
        d = Counter(barcodes)
        for i in d:
            heapq.heappush(heap, [-d[i], i])
        
        result = []

        while heap:
            # print(heap)
            count, element = heapq.heappop(heap)
            
            if count == 0:
                return result
            result.append(element)
            if heap:
                count1, element1 = heapq.heappop(heap)
                if count1 < 0:
                    result.append(element1)
                    heapq.heappush(heap, [count1+1, element1])
            heapq.heappush(heap, [count+1, element])

        return result
            