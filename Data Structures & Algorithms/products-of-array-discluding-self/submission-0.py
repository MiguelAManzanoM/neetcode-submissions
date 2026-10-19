class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n
        accum_left = 1
        accum_right = 1

        for i in range(n):
            products[i] = accum_left
            accum_left *= nums[i]

        for j in range(n - 1, -1, -1):
            products[j] *= accum_right
            accum_right *= nums[j]
        
        return products