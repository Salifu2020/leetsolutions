class Solution:
    def sumOfMultiples(self, n: int) -> int:
        lst = []

        for i in range(1,n+1):
            if i % 3 == 0:
                lst.append(i)
            elif i % 5 == 0:
                lst.append(i)
            elif i % 7 == 0:
                lst.append(i)

        return sum(lst)