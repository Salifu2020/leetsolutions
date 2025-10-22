class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        lst = []
        for key, v in counts.items():
            if v == 1:
                lst.append(key)

        if len(lst) >= k:
            return lst[k - 1]
        else:
            return ""
            