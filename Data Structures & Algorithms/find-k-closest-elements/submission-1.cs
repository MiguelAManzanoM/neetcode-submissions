public class Solution {
    public List<int> FindClosestElements(int[] arr, int k, int x) {
        int left = 0;
        int right = arr.Length - 1;

        // Reducimos la ventana hasta que el tamaño sea exactamente k
        // El tamaño actual es (right - left + 1)
        while (right - left + 1 > k) {
            // Calculamos distancias absolutas
            int distLeft = Math.Abs(arr[left] - x);
            int distRight = Math.Abs(arr[right] - x);

            // Si el de la izquierda está más lejos, lo descartamos
            // OJO: Si las distancias son iguales, el problema dice que 
            // prefiramos el número más pequeño (el de la izquierda).
            // Por eso solo movemos 'left' si es estrictamente mayor.
            if (distLeft > distRight) {
                left++;
            } else {
                right--;
            }
        }

        // Creamos la lista de resultado con los elementos que quedaron en la ventana
        List<int> result = new List<int>();
        for (int i = left; i <= right; i++) {
            result.Add(arr[i]);
        }

        return result;
    }
}