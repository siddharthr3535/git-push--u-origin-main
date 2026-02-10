class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        q = deque()
        def solve(q, set1):
            visited = set()
            while q:
                i,j = q.popleft()
                visited.add((i,j))
                set1.add((i,j))
                for di,dj in dir:
                    ni, nj = di + i, dj+ j
                    if 0<=ni<len(heights) and 0<=nj<len(heights[0]):
                        if heights[ni][nj] >= heights[i][j] and (ni,nj) not in visited:
                            q.append([ni,nj])
                            visited.add((ni,nj))
            return set1
            

        for i in range(len(heights)):
            q.append([i,0])
        for i in range(len(heights[0])):
            q.append([0,i])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        atlantic = solve(q, atlantic)
        t = len(heights[0]) -1
        q = deque()
        for i in range(len(heights)):
            q.append([i,t])
        t = len(heights) - 1
        for i in range(len(heights[0])):
            q.append([t,i])
        pacific = set()
        pacific = solve(q, pacific)
        result = []
        for i,j in pacific:
            if (i,j) in atlantic:
                result.append([i,j])
        return result
        
            

        
        
