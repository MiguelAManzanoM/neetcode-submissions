class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Creamos una matriz de (ROWS + 1) x (COLS + 1) llena de ceros
        self.pref = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Llenamos la matriz de suma prefija 2D
        for r in range(ROWS):
            for c in range(COLS):
                self.pref[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.pref[r][c + 1]
                    + self.pref[r + 1][c]
                    - self.pref[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Aplicamos la fórmula del Principio de Inclusión-Exclusión en O(1)
        return (
            self.pref[row2 + 1][col2 + 1]
            - self.pref[row1][col2 + 1]
            - self.pref[row2 + 1][col1]
            + self.pref[row1][col1]
        )