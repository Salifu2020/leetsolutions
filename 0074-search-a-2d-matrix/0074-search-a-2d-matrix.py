class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for row in matrix:
            if target in row:
                lst.append(row)


        return len(lst) > 0