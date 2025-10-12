import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10000)
        sys.set_int_max_str_digits(100000) 
        list_num = int(''.join(map(str, num)))

        list_num += k
        str_num = str(list_num)

        return list(map(int, str_num))
        