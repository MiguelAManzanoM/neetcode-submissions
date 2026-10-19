class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 1. Solo necesitamos saber cuánto mide la más corta para el bucle
        min_len = min(len(word1), len(word2))
        combined = []

        # 2. Intercalamos (Siempre word1 primero)
        for i in range(min_len):
            combined.append(word1[i])
            combined.append(word2[i])

        # 3. El Slicing Mágico:
        # Pegamos el resto de word1 Y el resto de word2.
        # Si una ya terminó, su slice será "" y no afectará nada.
        combined.append(word1[min_len:])
        combined.append(word2[min_len:])

        return "".join(combined)