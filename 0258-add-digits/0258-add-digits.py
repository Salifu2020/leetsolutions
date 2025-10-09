class Solution:
    def addDigits(self, num: int) -> int:
        total = sum(int(i) for i in str(num))

        i = len(str(total))

        while i > 0:
            total = sum(int(i) for i in str(total))
            i -= 1

        return total
        