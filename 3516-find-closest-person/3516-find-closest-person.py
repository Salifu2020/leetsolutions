class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        i = x
        count = 0
        j = y
        counter = 0
        while i != z:
            count += 1
            if i < z:
                i = i + 1
            else:
                i = i - 1

        while j != z:
            counter += 1
            if j > z:
                j = j - 1
            else:
                j = j + 1


        if count > counter:
            return 2
        elif count < counter:
            return 1
        else:
            return 0