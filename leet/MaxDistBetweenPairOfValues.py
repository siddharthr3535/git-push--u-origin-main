class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        def solve(i, num):
            l = i
            r = len(nums2) - 1
            result = 0
            while l <= r:
                mid = (l + r) // 2
                if nums2[mid] >= num:
                    result = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return result

        i = 0 
        j = 0
        for i in range(len(nums1)):
            j = solve(i, nums1[i])
            result = max(result, j - i)
        return result