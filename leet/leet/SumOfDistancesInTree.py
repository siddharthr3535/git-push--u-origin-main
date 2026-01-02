from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [1]*n
        result = [0] * n
        def solve(node, parent):
            for i in d[node]:
                if i == parent:
                    continue
                solve(i, node)
                count[node] = count[i] + count[node]
                result[node] += result[i] + count[i]
                
        def solve1(node, parent):
            for i in d[node]:
                if i == parent:
                    continue
                result[i] = result[node] - count[i] + (n - count[i])
                solve1(i, node)
        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        solve(0,-1)
        solve1(0,-1)
        
        return result