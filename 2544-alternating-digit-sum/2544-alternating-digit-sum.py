class Solution:
    def alternateDigitSum(self, n: int) -> int:
        lst = list(str(n))
        final = []
        for i in range(len(lst)):
            if i % 2 == 0:
                final.append(int(lst[i]))
            else:
                final.append(-int(lst[i]))

        return sum(final)