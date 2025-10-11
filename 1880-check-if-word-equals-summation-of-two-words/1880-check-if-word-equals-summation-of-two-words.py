class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        total1 = ''
        for ch in firstWord:
            if ch in alpha_list:
                total1 += str(alpha_list.index(ch))

        total2 = ''
        for ch2 in secondWord:
            if ch2 in alpha_list:
                total2 += str(alpha_list.index(ch2))

        total3 = ''
        for ch3 in targetWord:
            if ch3 in alpha_list:
                total3 += str(alpha_list.index(ch3))


        return int(total1) + int(total2) == int(total3)
        