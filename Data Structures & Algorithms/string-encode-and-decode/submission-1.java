class Solution {

    // Codifica una lista de cadenas a una sola cadena
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            // Concatena: longitud + "#" + palabra original
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    // Decodifica una sola cadena de vuelta a la lista de cadenas original
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            // indexOf busca el siguiente '#' empezando desde la posición 'i'
            int j = s.indexOf('#', i);
            
            // Extrae el número entre 'i' y la posición del '#'
            int length = Integer.parseInt(s.substring(i, j));
            
            // Extrae la palabra exacta basándose en la longitud
            String word = s.substring(j + 1, j + 1 + length);
            res.add(word);
            
            // Mueve el puntero para procesar la siguiente palabra
            i = j + 1 + length;
        }
        
        return res;
    }
}
