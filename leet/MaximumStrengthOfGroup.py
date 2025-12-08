from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        count = 0
        result = 1
        flag = False
        s = []
        if len(nums) == 1:
            return nums[0]
        while i < len(nums):
            while i < len(nums) and nums[i] < 0:
                count += 1
                s.append(nums[i])
                i+= 1
            if i < len(nums):
                if nums[i] != 0:
                    flag = True
                    result *= nums[i]
                i += 1
        if count > 1:
            if count % 2 == 0:
                for i in s:
                    flag = True
                    result *= i
            else:
                s = s[:-1]
                for i in s:
                    flag = True
                    result *= i
        if flag == True:
            return result
        return 0

        
            