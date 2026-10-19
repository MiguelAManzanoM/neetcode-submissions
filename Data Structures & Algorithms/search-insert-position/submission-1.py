class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculamos el punto medio
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # Caso ideal: encontramos el objetivo
                return mid
            elif nums[mid] < target:
                # El objetivo es mayor, descartamos la mitad izquierda
                left = mid + 1
            else:
                # El objetivo es menor, descartamos la mitad derecha
                right = mid - 1
                
        # Si no lo encontramos, 'left' es el índice correcto de inserción
        return left