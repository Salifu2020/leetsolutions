class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()

        s_reversed =''

        for item in lst:
            s_reversed += item[::-1] + ' '

        return s_reversed.rstrip()
        