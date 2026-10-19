class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        No retorna nada, modifica nums in-place.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                # Si encontramos un 0, lo mandamos a la sección izquierda
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                # Si es un 1, ya está en la sección central, seguimos avanzando
                i += 1
            else:
                # Si es un 2, lo mandamos a la sección derecha
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # Nota: no incrementamos 'i' aquí porque el elemento que 
                # intercambiamos desde 'right' podría ser un 0 o un 2, 
                # y necesitamos evaluarlo en la siguiente iteración.