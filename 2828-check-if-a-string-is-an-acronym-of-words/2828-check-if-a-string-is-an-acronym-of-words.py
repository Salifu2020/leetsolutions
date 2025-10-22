class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        lst = [i[0] for i in words]

        return ''.join(lst) == s
        