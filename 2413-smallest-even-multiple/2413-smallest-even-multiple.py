class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num_str = ''

        for i in range(1, 1543210):
            if i % 2 == 0 and i % n == 0:
                num_str += str(i)
                break
            else:
                num_str += '0'

        return int(num_str)
        