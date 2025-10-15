class Solution:
    def numberOfSteps(self, num: int) -> int:

        i = num
        count = 0
        while i != 0:

            if i % 2 == 0:
                i //= 2
            else:
                i -= 1
            count += 1

        return count
        