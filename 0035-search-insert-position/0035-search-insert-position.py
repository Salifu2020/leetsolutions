class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = []
        if target not in nums:
            nums.append(target)
            nums.sort()
            idx.append(nums.index(target))
        else:
            idx.append(nums.index(target))

        r = ''
        for i in idx:
            r += str(i)
        return int(r)
        