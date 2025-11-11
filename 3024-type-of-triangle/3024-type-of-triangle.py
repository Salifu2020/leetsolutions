class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        if len(set(nums)) == 1:
            return 'equilateral'

        lst = [nums[0] + nums[1] > nums[2], nums[0] + nums[2] > nums[1], nums[1] + nums[2] > nums[0]]

        if len(set(lst)) == 1 and len(set(nums)) == 2:
            return 'isosceles'
        elif len(set(lst)) == 1 and len(set(nums)) == 3:
            return 'scalene'

        return 'none'
