class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        new_list = []

        for word in lst:
            for char in word:
                if char.isdigit():
                    new_list.append(char)
        new_list.sort()

        final = ""
        for digit in new_list:
            for word in lst:
                if digit in word:
                    final += word.replace(digit, '') + ' '

        return final.rstrip()
        