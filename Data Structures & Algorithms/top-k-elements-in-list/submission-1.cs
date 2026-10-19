public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // 1. Contar frecuencias: O(N)
        var counts = new Dictionary<int, int>();
        foreach (var n in nums) {
            counts[n] = counts.GetValueOrDefault(n, 0) + 1;
        }

        // 2. Usar una Priority Queue (Min-Heap): O(N log K)
        // El primer parámetro es el VALOR (el número), 
        // el segundo es la PRIORIDAD (la frecuencia).
        var pq = new PriorityQueue<int, int>();

        foreach (var entry in counts) {
            pq.Enqueue(entry.Key, entry.Value);
            
            // Si superamos K, eliminamos al de MENOR frecuencia
            if (pq.Count > k) {
                pq.Dequeue();
            }
        }

        // 3. Extraer los resultados: O(K log K)
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.Dequeue();
        }

        return res;
    }
}