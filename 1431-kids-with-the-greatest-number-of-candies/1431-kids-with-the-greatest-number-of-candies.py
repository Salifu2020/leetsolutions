class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for cand in candies:

            result.append(cand + extraCandies >= max(candies))

        return result
        