class Solution {
    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int i = 0;
        
        while (i <= right) {
            if (nums[i] == 0) {
                // Intercambiar nums[i] y nums[left]
                int temp = nums[i];
                nums[i] = nums[left];
                nums[left] = temp;
                
                left++;
                i++;
            } else if (nums[i] == 1) {
                // El 1 está en la posición correcta
                i++;
            } else {
                // Intercambiar nums[i] y nums[right]
                int temp = nums[i];
                nums[i] = nums[right];
                nums[right] = temp;
                
                right--;
                // No incrementamos 'i' aquí
            }
        }
    }
}