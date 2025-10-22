class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for num in nums:
            if num < 0 and abs(num) in nums:
                return abs(num)

        return -1
        