class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()

        set_nums = set(nums)
        lst = list(set_nums)
        lst.sort()

        if len(lst) < 3:
            return max(lst)

        return lst[-3]
        