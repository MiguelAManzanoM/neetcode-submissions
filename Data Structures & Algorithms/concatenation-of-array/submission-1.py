class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (n * 2)

        for i in range(n):
            result[i] = nums[i]
            result[n + i] = nums[i]

        return result