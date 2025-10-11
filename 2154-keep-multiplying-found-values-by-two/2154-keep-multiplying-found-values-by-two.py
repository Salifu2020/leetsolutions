class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original

        total = original
        while total in nums:
            total *= 2

        return total
        