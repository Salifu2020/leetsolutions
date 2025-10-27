class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split()
        final = [int(string) for string in lst if string.isdigit()]

        if len(set(final)) != len(final):
            return False

        return  final == sorted(final)
        