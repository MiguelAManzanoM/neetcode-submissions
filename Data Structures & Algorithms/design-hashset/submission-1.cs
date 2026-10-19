public class MyHashSet {
    
    // 1. Definimos la clase del nodo de forma privada (Encapsulamiento)
    private class ListNode {
        public int key;
        public ListNode next;
        
        // Constructor con valor por defecto
        public ListNode(int key = -1) {
            this.key = key;
            this.next = null;
        }
    }

    // 2. Declaramos el arreglo de cubetas y el tamaño
    private ListNode[] buckets;
    private int size = 1000;

    public MyHashSet() {
        // En C#, instanciar el arreglo solo crea "espacios vacíos" (nulls).
        buckets = new ListNode[size];
        
        // A diferencia de Python donde usamos list comprehension, 
        // aquí necesitamos un bucle explícito para llenar cada espacio con un nodo centinela.
        for (int i = 0; i < size; i++) {
            buckets[i] = new ListNode(); 
        }
    }

    // 3. Nuestra función Hash (Load Balancer)
    private int Hash(int key) {
        return key % size;
    }

    public void Add(int key) {
        ListNode cur = buckets[Hash(key)];
        
        while (cur.next != null) {
            if (cur.next.key == key) {
                return; // Si ya existe, salimos sin hacer nada
            }
            cur = cur.next;
        }
        
        // Si llegamos al final del ciclo y no estaba, lo agregamos
        cur.next = new ListNode(key);
    }

    public void Remove(int key) {
        ListNode cur = buckets[Hash(key)];
        
        while (cur.next != null) {
            if (cur.next.key == key) {
                // Hacemos el "bypass". El Garbage Collector de .NET 
                // destruirá el nodo desconectado automáticamente.
                cur.next = cur.next.next;
                return;
            }
            cur = cur.next;
        }
    }

    public bool Contains(int key) {
        ListNode cur = buckets[Hash(key)];
        
        while (cur.next != null) {
            if (cur.next.key == key) {
                return true;
            }
            cur = cur.next;
        }
        
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */