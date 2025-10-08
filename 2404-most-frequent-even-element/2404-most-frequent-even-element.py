from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if len(nums) == 1 and nums[0] % 2 == 0:
            return nums[0]
        lst = []
        for x in nums:
            if x % 2 == 0 and counter[x] >= 1:
                lst.append(x)
                lst.sort()


        counts = Counter(lst)
        if len(lst) >= 1:
            return counts.most_common(1)[0][0]

        return -1
        