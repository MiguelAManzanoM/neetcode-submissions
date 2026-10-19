class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. Configuramos los tres punteros al final de sus respectivas zonas
        p1 = m - 1         # Último elemento válido de nums1
        p2 = n - 1         # Último elemento de nums2
        p = m + n - 1      # Última posición disponible en el buffer total de nums1

        # 2. Recorremos mientras haya elementos en nums2
        # (Si nums2 se vacía, los elementos que quedan en nums1 ya están ordenados en su lugar)
        while p2 >= 0:
            # Si p1 sigue siendo válido y su número es el "ganador" (más grande)
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            # Si p2 es el ganador (o si ya nos acabamos los elementos de nums1)
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            # Sin importar quién ganó, movemos el puntero de escritura hacia la izquierda
            p -= 1