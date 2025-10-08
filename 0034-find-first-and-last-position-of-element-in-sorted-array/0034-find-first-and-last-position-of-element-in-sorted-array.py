class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []

        for i in range(len(nums)):
            if nums[i] == target:
                lst.append(i)

        if len(lst) == 0:
            return [-1, -1]
        elif len(lst) == 1:
            return [lst[0], lst[0]]

        return lst[::len(lst) - 1]
        