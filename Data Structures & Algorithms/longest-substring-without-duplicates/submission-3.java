class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Un arreglo de 128 posiciones para caracteres ASCII. 
        // Actúa como un diccionario ultra rápido.
        int[] charIndex = new int[128];
        
        // Llenamos el arreglo con -1. 
        // Esto es vital porque el índice 0 es una posición válida en la cadena,
        // así diferenciamos un carácter no visto (-1) de uno visto en el inicio (0).
        Arrays.fill(charIndex, -1);
        
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            // Si el carácter ya fue visto y su índice está dentro de la ventana actual (>= left)
            if (charIndex[currentChar] >= left) {
                // Movemos 'left' directamente una posición adelante del duplicado
                left = charIndex[currentChar] + 1;
            }
            
            // Calculamos la longitud de la ventana actual y actualizamos el máximo
            maxLength = Math.max(maxLength, right - left + 1);
            
            // Guardamos (o sobrescribimos) el índice actual del carácter
            charIndex[currentChar] = right;
        }
        
        return maxLength;
    }
}

