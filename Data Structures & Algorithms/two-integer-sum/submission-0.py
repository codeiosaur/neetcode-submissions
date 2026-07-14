class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_indices:
                return sorted([i, num_indices[complement]])
            else:
                num_indices[nums[i]] = i