class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for sublist in matrix:
            lst += sublist

        lst.sort()
        return lst[k-1]
        