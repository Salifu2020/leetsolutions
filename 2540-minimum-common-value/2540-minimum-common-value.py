class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        inter_set = set1 & set2

        if not inter_set:
            return -1

        return min(inter_set)