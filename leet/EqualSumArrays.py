class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = sum(nums1)
        total2 = sum(nums2)
        if total1 == total2:
            return 0
        if total1 < total2:
            nums = [(6-num) for num in nums1] + [(num - 1) for num in nums2]
        else:
            nums = [(num - 1) for num in nums1] + [(6-num) for num in nums2]
        
        nums.sort(reverse = True)

        diff = abs(total1 - total2)

        result = 0

        # print(nums)
        for i in range(len(nums)):
            diff -= nums[i]
            result += 1
            if diff <= 0:
                return result
        if diff <= 0:
            return result
        return -1