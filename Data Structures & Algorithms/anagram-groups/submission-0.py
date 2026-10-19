class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Un diccionario normal nativo de Python
        anagram_map = {}
        
        for s in strs:
            # 1. Creamos una lista de 26 ceros (uno para cada letra)
            count = [0] * 26
            
            # 2. Llenamos las frecuencias de la palabra actual
            for c in s:
                # ord() obtiene el valor ASCII de la letra
                count[ord(c) - ord('a')] += 1
            
            # 3. Convertimos la lista a tupla para usarla como llave
            key = tuple(count)
            
            # 4. Si la tupla no está en el diccionario, la inicializamos
            if key not in anagram_map:
                anagram_map[key] = []
            
            # 5. Agregamos la palabra original
            anagram_map[key].append(s)
            
        # 6. Devolvemos los valores del diccionario como una lista de listas
        return list(anagram_map.values())