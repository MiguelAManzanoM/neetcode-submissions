class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        while l < r:
            # Calculamos el punto medio previniendo overflow de enteros
            m = l + (r - l) // 2
            
            if nums[m] < target:
                # El valor objetivo está más a la derecha
                l = m + 1
            else:
                # El objetivo es menor o igual, reducimos el límite derecho
                r = m
                
        # Cuando 'l == r', apunta exactamente a la posición de inserción
        return l