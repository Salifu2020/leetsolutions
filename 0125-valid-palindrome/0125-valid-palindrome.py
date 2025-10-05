class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == ' ':
                continue
            lst.append(i)

        for j in lst:
            if not j.isalnum():
                lst.remove(j)

        full_str = ''.join(ch for ch in lst if ch.isalnum()).lower()

        return full_str == full_str[::-1]
        