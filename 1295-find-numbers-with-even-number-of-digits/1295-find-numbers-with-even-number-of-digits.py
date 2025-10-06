class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_list = []

        for num in nums:
            str_list.append(str(num))

        counter = 0
        for element in str_list:

            if len(element) % 2 == 0:
                counter += 1

        return counter
        