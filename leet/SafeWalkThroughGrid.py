class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        result = False
        best = []
        for i in range(len(grid)):
            sample = [-1] * len(grid[i])
            best.append(sample)
        def solve(i, j, current):
            nonlocal result
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return False
            current -= grid[i][j]
            if current <= 0:
                return False
            if current <= best[i][j]:
                return False
            best[i][j] = current
            if i == len(grid) - 1 and j == len(grid[i]) - 1:
                result = True

            if solve(i + 1, j , current):
                return True
            if solve(i - 1, j , current):
                return True
            if solve(i , j+ 1, current):
                return True

            if solve(i , j - 1 , current):
                return True
            return False
        
        
        solve(0 , 0 , health)
        return result
            