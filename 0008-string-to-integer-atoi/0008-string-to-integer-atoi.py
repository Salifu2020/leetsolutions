class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '' or s[0].isalpha():
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]


        new_s = ''
        for char in s:
            if char.isdigit():
                new_s += char
            else:
                break
        
        if not new_s:
            return 0


        int_s = int(new_s) * sign

        INT_MIN = -2**31  
        INT_MAX = 2**31 - 1
        if int_s < INT_MIN:
            return INT_MIN
        if int_s > INT_MAX:
            return INT_MAX

        return int_s