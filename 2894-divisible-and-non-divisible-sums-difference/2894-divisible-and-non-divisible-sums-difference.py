class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        lst = [num for num in range(1, n + 1) if num % m != 0]
        lst2 = [i for i in range(1, n + 1) if i % m == 0]

        return sum(lst) - sum(lst2)
        