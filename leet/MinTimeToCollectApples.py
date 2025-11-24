from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        
        def solve(node, prev, cost):
            subCost = 0
            
            for i in d[node]:
                if i == prev:
                    continue
                subCost += solve(i, node, 2)
            if subCost == 0 and hasApple[node] != True:
                return 0

            return subCost + cost
        return solve(0, - 1, 0 )