class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for num in nums:
            if counter[num] == 3:
                continue
            return num

        return -1
        