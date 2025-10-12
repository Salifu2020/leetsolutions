class Solution:
    def countSeniors(self, details: List[str]) -> int:
        lst = []

        for detail in details:
            lst.append(detail[-4:-2])

        count = 0
        for num in lst:
            if int(num) > 60:
                count += 1

        return count
            