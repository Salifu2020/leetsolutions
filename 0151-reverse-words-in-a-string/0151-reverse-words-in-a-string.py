class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()

        s_reversed = " ".join(lst[::-1])

        return s_reversed.rstrip()
        