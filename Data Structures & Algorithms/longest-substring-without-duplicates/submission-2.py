class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # Si el carácter ya está en el diccionario y su índice anterior 
            # está dentro de nuestra ventana actual (>= left)
            if char in char_index and char_index[char] >= left:
                # Hacemos que el puntero izquierdo salte un espacio adelante del duplicado
                left = char_index[char] + 1
            
            # Registramos/actualizamos el índice más reciente del carácter
            char_index[char] = right
            
            # Calculamos el tamaño de la ventana actual y actualizamos el máximo
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length


