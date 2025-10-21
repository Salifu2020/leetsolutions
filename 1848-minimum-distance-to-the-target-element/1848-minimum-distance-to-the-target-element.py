class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        lst = []

        for i in range(len(nums)):
            if nums[i] == target:
                lst.append(abs(i - start))

        return min(lst)
        