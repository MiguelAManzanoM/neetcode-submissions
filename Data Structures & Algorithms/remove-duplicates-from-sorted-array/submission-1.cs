public class Solution {
    public int RemoveDuplicates(int[] nums) {
        // Validación defensiva: Buena práctica en entrevistas de .NET
        if (nums == null || nums.Length == 0) {
            return 0;
        }

        // Tu puntero escritor arranca en 0
        int writer = 0;

        // El lector arranca en 1. 
        // Nota: nums.Length es una propiedad O(1), no un método como len()
        for (int i = 1; i < nums.Length; i++) {
            
            // Si encontramos un número nuevo...
            if (nums[i] != nums[writer]) {
                writer++;               // 1. Movemos el escritor adelante
                nums[writer] = nums[i]; // 2. Escribimos el nuevo valor
            }
        }
        
        // Retornamos la cantidad de elementos (índice + 1)
        return writer + 1;
    }
}