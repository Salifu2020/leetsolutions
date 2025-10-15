class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(map(int, str(n)))

        product = 1
        for num in lst:
            product *= num


        return product - sum(lst)
        