# 1. El "Vagón" ahora carga tanto la llave como el valor
class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        # Creamos nuestras 1000 cubetas
        self.size = 1000
        # Todas inicializadas con un Nodo Dummy (Centinela)
        self.buckets = [ListNode() for _ in range(self.size)]

    # El Load Balancer
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # Nos dirigimos a la cubeta correcta
        cur = self.buckets[self._hash(key)]
        
        # Caminamos por la lista ligada buscando la llave
        while cur.next:
            if cur.next.key == key:
                # ¡La encontramos! Actualizamos el valor y terminamos
                cur.next.val = value
                return
            cur = cur.next
            
        # Si llegamos al final y no estaba, creamos un nuevo nodo con la llave y el valor
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.buckets[self._hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                # Si la encontramos, retornamos su "payload"
                return cur.next.val
            cur = cur.next
            
        # El problema pide retornar -1 si la llave no existe
        return -1

    def remove(self, key: int) -> None:
        cur = self.buckets[self._hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                # Bypass de red: desconectamos el nodo objetivo
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)