class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            # Caso base: un arreglo de 1 o 0 elementos ya está ordenado
            if len(arr) <= 1:
                return arr
            
            # 1. DIVIDIR: Encontrar la mitad y partir el arreglo en dos
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            # Llamada recursiva para ordenar ambas mitades
            merge_sort(left_half)
            merge_sort(right_half)
            
            # 2. CONQUISTAR (Mezclar): Punteros para left_half (i), right_half (j) y arr (k)
            i = 0
            j = 0
            k = 0
            
            # Comparamos elementos de ambas mitades y los sobreescribimos en arr
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                
            # Si sobraron elementos en la mitad izquierda, los agregamos
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
                
            # Si sobraron elementos en la mitad derecha, los agregamos
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                
            return arr

        return merge_sort(nums)
        