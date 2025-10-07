class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        str1 = []
        for i in range(n):
            j = n -i
            if j > 0 and not '0' in str(i) and not '0' in str(j):
                str1 = [i, j]
                str1.sort()

        return str1