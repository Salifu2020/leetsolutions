class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_indices = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        target_indices = [j, i]
                        break

        return target_indices