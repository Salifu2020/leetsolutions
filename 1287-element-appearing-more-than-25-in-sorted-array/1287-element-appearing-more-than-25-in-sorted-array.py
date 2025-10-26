class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_freq = 0.25*len(arr)

        counts =    Counter(arr)

        num = ''

        for key, value in counts.items():
            if value > num_freq:
                num += str(key)


        return int(num)
        