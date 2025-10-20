class Solution:
    def averageValue(self, nums: List[int]) -> int:
        lst = []
        for num in nums:
            if num % 3 == 0:
                lst.append(num)

        if len(lst) == 0:
            return 0

        return int(sum(lst) / len(lst))
        