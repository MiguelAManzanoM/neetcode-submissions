public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // 1. Conteo de frecuencias
        var counts = new Dictionary<int, int>();
        foreach (int n in nums) {
            // Usamos GetValueOrDefault para hacerlo más limpio (Sugerencia de NeetCode)
            counts[n] = counts.GetValueOrDefault(n, 0) + 1;
        }

        // 2. Bucket Sort (Arreglo de listas)
        // El tamaño es nums.Length + 1 porque la frecuencia máxima es N
        var freq = new List<int>[nums.Length + 1];
        
        foreach (var entry in counts) {
            int num = entry.Key;
            int count = entry.Value;
            
            if (freq[count] == null) {
                freq[count] = new List<int>();
            }
            freq[count].Add(num);
        }

        // 3. Recolección de los Top K
        var res = new List<int>();
        // Recorremos de atrás hacia adelante (mayores frecuencias primero)
        for (int i = freq.Length - 1; i >= 0; i--) {
            if (freq[i] != null) {
                foreach (int num in freq[i]) {
                    res.Add(num);
                    if (res.Count == k) {
                        return res.ToArray();
                    }
                }
            }
        }

        return res.ToArray();
    }
}