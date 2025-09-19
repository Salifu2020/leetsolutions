class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        num_str = str(x)
        num_list = list(num_str)

        int_list = []
        for num in num_list:
            int_list.append(int(num))

        int_list.reverse()

        # if int_list[0] == 0:
         #   int_list.remove(int_list[0])

        str_list = ''
        for num in int_list:
            str_list += str(num)

        final_int = int(str_list)

        if final_int < -2**31 or final_int > 2**31:
            return 0
        else:
            return final_int * sign
