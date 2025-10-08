from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)

        lst = []
        for i in nums:
            if counts[i] == 1:
                lst.append(i)


        return sum(lst)