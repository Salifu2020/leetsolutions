class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = Counter(nums)


        for num in nums:
            if counts[num] == len(nums) // 2:
                return num


        return -1
        