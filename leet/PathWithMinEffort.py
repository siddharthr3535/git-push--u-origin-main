from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, [0,0,0])
        dp = []
        visited = set()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        while heap:
            dis, i,j = heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if (i,j) == (len(heights)-1, len(heights[0]) -1):
                return dis
            for di, dj in dir:
                ni, nj = di + i, dj + j
                if (ni,nj) in visited:
                    continue
                if 0<= ni < len(heights) and 0<=nj < len(heights[0]):
                    newdis = max(dis, abs(heights[ni][nj] - heights[i][j]))
                    heapq.heappush(heap, [newdis, ni, nj])
