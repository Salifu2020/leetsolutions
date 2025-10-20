class Solution:
    def countDigits(self, num: int) -> int:
        lst = list(str(num))

        count = 0

        for val in lst:
            if num % int(val) == 0:
                count += 1

        return count
        