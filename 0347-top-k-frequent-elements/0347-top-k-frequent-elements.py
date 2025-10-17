class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        lst = counts.most_common(k)
        final = []
        for item in lst:
            final.append(item[0])

        return final
        