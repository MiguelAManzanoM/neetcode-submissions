public class Solution {
    // Nota que el método es 'void', lo que significa que modifica in-place 
    // y no devuelve un nuevo arreglo.
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        // 1. Configuramos los punteros al final de los elementos válidos
        int p1 = m - 1;
        int p2 = n - 1;
        
        // El puntero de escritura va al final del buffer total
        int p = m + n - 1;

        // 2. Recorremos mientras haya datos en nums2
        while (p2 >= 0) {
            // Si p1 es válido y su número es mayor, lo colocamos al final
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p] = nums1[p1];
                p1--; // En C# usamos el operador de decremento directo
            } 
            // Si p2 es mayor, o si ya no quedan elementos en p1
            else {
                nums1[p] = nums2[p2];
                p2--;
            }
            
            // Siempre movemos el puntero de escritura hacia la izquierda
            p--;
        }
    }
}