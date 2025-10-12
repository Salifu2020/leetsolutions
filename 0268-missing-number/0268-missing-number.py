class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = 0
        for num in range(len(nums)+1):
            if num not in nums:
                number += num

        return number
        