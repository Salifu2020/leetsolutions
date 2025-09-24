class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_string_int = ''
        for num in digits:
            my_string_int += str(num)

        old_string = int(my_string_int)
        old_string += 1

        new_old_string = str(old_string)
        new_list = []
        for num in new_old_string:
            new_list.append(int(num))

        return new_list
        