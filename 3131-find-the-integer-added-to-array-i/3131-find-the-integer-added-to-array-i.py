class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        return nums2[0] - nums1[0]