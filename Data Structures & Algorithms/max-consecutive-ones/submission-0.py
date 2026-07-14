class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_chain = 0
        chain = 0
        for i in range(len(nums)):
            chain = chain + 1 if nums[i] == 1 else 0
            max_chain = max(max_chain, chain)
        return max_chain
        