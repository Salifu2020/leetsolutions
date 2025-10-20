class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        lst = list(str(x))
        lst2 = [int(x) for x in lst]

        lst_sum = sum(lst2)

        if x % lst_sum == 0:
            return lst_sum
        else:
            return -1
        