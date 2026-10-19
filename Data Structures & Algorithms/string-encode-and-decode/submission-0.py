class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Formato: [longitud] + "#" + [cadena]
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Encontrar dónde está el delimitador '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extraer la longitud de la palabra (todo lo que está antes del '#')
            length = int(s[i:j])
            
            # El inicio de la palabra es j + 1
            # El final de la palabra es j + 1 + length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Mover el puntero 'i' al inicio del próximo bloque
            i = j + 1 + length
            
        return res