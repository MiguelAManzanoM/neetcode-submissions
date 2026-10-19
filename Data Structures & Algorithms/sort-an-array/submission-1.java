class Solution {
    public int[] sortArray(int[] nums) {
        // Creamos el arreglo temporal una sola vez y lo pasamos por referencia
        int[] temp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1, temp);
        return nums;
    }

    private void mergeSort(int[] nums, int left, int right, int[] temp) {
        // Caso base: si el sub-arreglo tiene 1 o 0 elementos, ya está ordenado
        if (left >= right) {
            return;
        }

        // 1. DIVIDIR: Encontramos la mitad (evitando desbordamiento de enteros)
        int mid = left + (right - left) / 2;

        // Llamadas recursivas para ordenar ambas mitades
        mergeSort(nums, left, mid, temp);
        mergeSort(nums, mid + 1, right, temp);

        // 2. CONQUISTAR: Mezclamos las mitades ordenadas
        merge(nums, left, mid, right, temp);
    }

    private void merge(int[] nums, int left, int mid, int right, int[] temp) {
        // Copiamos los elementos de esta sección al arreglo temporal
        for (int i = left; i <= right; i++) {
            temp[i] = nums[i];
        }

        int i = left;      // Puntero para la mitad izquierda
        int j = mid + 1;   // Puntero para la mitad derecha
        int k = left;      // Puntero para escribir en el arreglo original

        // Comparamos y mezclamos tomando el menor de ambos lados
        while (i <= mid && j <= right) {
            if (temp[i] <= temp[j]) {
                nums[k] = temp[i];
                i++;
            } else {
                nums[k] = temp[j];
                j++;
            }
            k++;
        }

        // Si sobraron elementos en la mitad izquierda, los copiamos
        while (i <= mid) {
            nums[k] = temp[i];
            i++;
            k++;
        }
        
        // Nota: No necesitamos un bucle para los sobrantes de la mitad derecha, 
        // porque ya se encuentran en su posición final correcta en 'nums'.
    }
}