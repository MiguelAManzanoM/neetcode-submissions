class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> triplets = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            // 1. Optimización que ya viste: si el número es positivo, no hay nada que buscar
            if (nums[i] > 0) {
                break;
            }

            // 2. Evitar duplicados para el primer número (nums[i])
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // Salta esta iteración si es igual al anterior
            }

            // 3. Los punteros nacen DENTRO del for, justo a la derecha de i
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum < 0) {
                    // La suma es muy pequeña, necesitamos valores más grandes -> movemos left
                    left++;
                } else if (sum > 0) {
                    // La suma es muy grande, necesitamos valores más pequeños -> movemos right
                    right--;
                } else {
                    // 1. Guardar el triplete correcto
                    triplets.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // 2. Mover ambos punteros
                    left++;
                    right--;

                    // 3. Saltar duplicados de 'left'
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }

                    // 4. Saltar duplicados de 'right'
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
            }
        }
        
        return triplets;
    }
}
