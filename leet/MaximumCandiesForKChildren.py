class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            return 0
        left , right= 1, total//k

        while left <= right:
            m = (left + right)//2
            count = 0
            for i in candies:
                count += i//m
                if count >= k:
                    break
            if count >= k:
                result = m
                left = m + 1
            else:
                right = m - 1
        return result