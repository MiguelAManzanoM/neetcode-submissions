public class MyStack {
    
    // Declaramos nuestra única cola
    private Queue<int> queue;

    public MyStack() {
        queue = new Queue<int>();
    }
    
    public void Push(int x) {
        // 1. Añadimos el nuevo elemento al final de la cola
        queue.Enqueue(x);
        
        // 2. Rotamos la cola (tamaño - 1) veces
        int rotations = queue.Count - 1;
        for (int i = 0; i < rotations; i++) {
            // Sacamos del frente y lo volvemos a meter por atrás
            queue.Enqueue(queue.Dequeue());
        }
    }
    
    public int Pop() {
        // El elemento "top" siempre estará al frente gracias a la rotación
        return queue.Dequeue();
    }
    
    public int Top() {
        // Peek() nos permite ver el elemento al frente sin sacarlo
        return queue.Peek();
    }
    
    public bool Empty() {
        // La pila está vacía si la cola no tiene elementos
        return queue.Count == 0;
    }
}



/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */