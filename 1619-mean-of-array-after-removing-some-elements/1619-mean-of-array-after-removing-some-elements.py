class Solution:
    def trimMean(self, arr: List[int]) -> float:
        five_percent = int(len(arr) * 0.05)
        arr.sort()

        arr1 = arr[five_percent : -five_percent]

        return sum(arr1) / len(arr1)
        