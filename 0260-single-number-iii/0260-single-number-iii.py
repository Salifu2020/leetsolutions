class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        lst = []
        for num in nums:
            if counter[num] != 2:
                lst.append(num)

        return lst
        