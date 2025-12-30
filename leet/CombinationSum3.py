class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def solve(i, current, currentSum):
            if currentSum == n and len(current) == k:
                result.append(current.copy())
                return
            if i > 9 or len(current) > k or currentSum > n:
                return
            current.append(i)
            solve(i+1, current, currentSum + i)
            current.pop()
            solve(i + 1, current, currentSum)
        solve(1, [],0)
        return result