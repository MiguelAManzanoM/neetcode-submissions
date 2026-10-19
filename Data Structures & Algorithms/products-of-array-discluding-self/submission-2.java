class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] products = new int[n];
        int accum_left = 1;
        int accum_right = 1;

        for(int i = 0; i < n; i++) {
            products[i] = accum_left;
            accum_left *= nums[i];
        }

        for(int j = n - 1; j >= 0; j--) {
            products[j] *= accum_right;
            accum_right *= nums[j];
        }
        
        return products;
    }
}  

