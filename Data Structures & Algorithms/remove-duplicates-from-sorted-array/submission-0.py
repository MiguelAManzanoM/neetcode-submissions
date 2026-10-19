class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[writer]:
                writer += 1
                nums[writer] = nums[i]
                
        return writer + 1