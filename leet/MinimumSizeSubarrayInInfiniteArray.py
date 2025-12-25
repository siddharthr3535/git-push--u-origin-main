class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        prefix = {0 : -1}

        size , target = divmod(target, sum(nums))

        if target == 0:
            return len(nums) * size

        current = 0
        result = float('inf')
        for i, element in enumerate(nums * 2):
            current += element
            if current - target in prefix:
                result = min(result, i - prefix[current-target])
            prefix[current] = i

        if result == float('inf'):
            return -1
        return len(nums) * size + result