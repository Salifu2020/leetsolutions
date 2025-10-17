class Solution:
    def maxDifference(self, s: str) -> int:
        lst = list(s)

        counter = Counter(lst)
        top_two = counter.most_common(3)
        lst2 = []

        for i in top_two:
            lst2.append(i[1])

        final = []
        for num in lst2:
            if num % 2 == 0:
                final.append(num)
                break

        for num in lst2:
            if num % 2 == 1:
                final.append(num)
                break

        return final[1] - final[0]