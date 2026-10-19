public class Solution {
    public int Search(int[] nums, int target) {
        // 1. Definimos nuestros límites (punteros)
        int left = 0;
        int right = nums.Length - 1;

        while (left <= right) {
            // 2. Calculamos el punto medio de forma segura
            // Usamos esta fórmula para evitar el Integer Overflow en arreglos gigantes
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid; // ¡Lo encontramos!
            }
            
            if (target < nums[mid]) {
                // El objetivo es menor, descartamos la mitad derecha
                right = mid - 1;
            } else {
                // El objetivo es mayor, descartamos la mitad izquierda
                left = mid + 1;
            }
        }

        // 3. Si el bucle termina, el elemento no existe
        return -1;
    }
}