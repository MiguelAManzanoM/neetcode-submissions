from collections import deque

class MyStack:
    def __init__(self):
        # Usamos deque que permite operaciones O(1) en ambos extremos
        self.queue = deque()

    def push(self, x: int) -> None:
        # 1. Añadimos el elemento al final
        self.queue.append(x)
        # 2. Rotamos la cola para que el nuevo elemento quede al frente
        # Esto reacomoda los elementos anteriores detrás del nuevo
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # El elemento "superior" de la pila ya está al frente de la cola
        return self.queue.popleft()
        
    def top(self) -> int:
        # Simplemente miramos el frente de la cola
        return self.queue[0]
        
    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()