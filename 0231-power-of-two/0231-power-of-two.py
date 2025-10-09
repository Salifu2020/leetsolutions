class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        nono = ''
        for i in itertools.count(0):
                if 2**i == n:
                    return True

                if 2**i > n:
                    return False

        return bool(nono)

        