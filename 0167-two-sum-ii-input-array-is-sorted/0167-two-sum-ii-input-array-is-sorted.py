class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            add_num = numbers[left] + numbers[right]
            if add_num == target:
                return [left + 1, right + 1]
            elif add_num < target:
                left = left + 1
            else:
                right = right - 1


        return [-1]
        