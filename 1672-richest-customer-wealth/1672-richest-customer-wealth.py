class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst = []

        for lists in accounts:
            lst.append(sum(lists))

        return max(lst)
        