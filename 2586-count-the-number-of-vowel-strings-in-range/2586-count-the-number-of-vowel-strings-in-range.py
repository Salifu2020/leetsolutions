class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        lst = words[left:right+1]
        count = 0
        for word in lst:
            if word[0] in vowels and word[-1] in vowels:
                count += 1

        return count
        