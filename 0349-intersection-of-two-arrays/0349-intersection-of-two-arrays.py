class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_list1 = set(nums1)
        set_list2 = set(nums2)

        inter_set = set_list1.intersection(set_list2)

        list_set = list(inter_set)

        return list_set
        