class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            nums[left] **= 2
            left += 1

        nums.sort()

        return nums
        