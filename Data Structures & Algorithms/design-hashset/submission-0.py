# Definimos nuestro "Vagón" para la lista ligada
class ListNode:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        # Creamos 1000 cubetas. (El número es arbitrario, suele ser un número primo)
        self.size = 1000
        
        # Llenamos nuestro arreglo con Nodos Dummy para asegurar que 
        # ninguna cubeta esté "vacía" (None), todas empiezan con un centinela.
        self.buckets = [ListNode() for _ in range(self.size)]

    # Nuestra función matemática (Load Balancer)
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        # 1. Encontramos la cubeta correcta
        cur = self.buckets[self._hash(key)]
        
        # 2. Caminamos por la lista ligada
        while cur.next:
            # Si ya existe, no hacemos nada (es un Set, no permite duplicados)
            if cur.next.key == key:
                return 
            cur = cur.next
            
        # 3. Si llegamos al final y no estaba, lo enganchamos
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.buckets[self._hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                # ¡Magia de SRE! Hacemos un "bypass" de red.
                # Desconectamos el nodo objetivo saltándonoslo.
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.buckets[self._hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
            
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)