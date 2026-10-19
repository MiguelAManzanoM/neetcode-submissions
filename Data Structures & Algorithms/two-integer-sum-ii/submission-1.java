class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        
        while (left < right) {
            int currentSum = numbers[left] + numbers[right];
            
            if (currentSum == target) {
                // Se suman 1 a los índices porque el problema exige 1-indexed
                return new int[] {left + 1, right + 1};
            } else if (currentSum > target) {
                // Si la suma es muy grande, reducimos el número mayor
                right--;
            } else {
                // Si la suma es muy pequeña, aumentamos el número menor
                left++;
            }
        }
        
        // El problema garantiza que siempre habrá una solución, 
        // pero el compilador de Java requiere un retorno por defecto.
        return new int[0];
    }
}