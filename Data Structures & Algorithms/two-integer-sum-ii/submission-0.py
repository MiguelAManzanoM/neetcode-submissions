class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # El problema exige retornar índices basados en 1 (1-indexed)
                return [left + 1, right + 1]
            elif current_sum > target:
                # La suma es muy grande, reducimos el número mayor
                right -= 1
            else:
                # La suma es muy pequeña, aumentamos el número menor
                left += 1