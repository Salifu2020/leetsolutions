class Solution:
    def isPalindrome(self, x: int) -> bool:
        my_list = list(str(x))

        new_list = my_list[::-1]
        if new_list == my_list:
            return True
        else:
            return False
            