public class Solution {
    public string MergeAlternately(string word1, string word2) {
        // 1. Usamos StringBuilder para eficiencia de memoria O(n + m)
        // Opcional: Podemos pre-definir la capacidad total para evitar redimensionamientos
        StringBuilder result = new StringBuilder(word1.Length + word2.Length);
        
        int n1 = word1.Length;
        int n2 = word2.Length;
        // Determinamos el punto de parada para el intercalado
        int minLen = Math.Min(n1, n2);

        // 2. Fase de Sincronía: Intercalamos caracteres
        for (int i = 0; i < minLen; i++) {
            result.Append(word1[i]);
            result.Append(word2[i]);
        }

        // 3. Fase de Remanente: Agregamos lo que sobró
        // En C# no hay slicing directo como [minLen:], usamos Substring
        if (n1 > n2) {
            result.Append(word1.Substring(minLen));
        } else if (n2 > n1) {
            result.Append(word2.Substring(minLen));
        }

        return result.ToString();
    }
}