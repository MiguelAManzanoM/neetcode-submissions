class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }
        
        int[] indegree = new int[numCourses];
        
        // Construir grafo y contar cuántos prerrequisitos entrantes tiene cada curso
        for (int[] p : prerequisites) {
            int course = p[0];
            int pre = p[1];
            adj.get(pre).add(course); // pre -> course
            indegree[course]++;       // course tiene un prerrequisito más
        }
        
        // 1. Meter a la cola todos los cursos que no tienen prerrequisitos (indegree == 0)
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int completed = 0;
        
        // 2. Procesar la cola
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            completed++;
            
            // Reducir en 1 el indegree de los cursos que dependían del curso actual
            for (int neighbor : adj.get(curr)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor); // ¡Quedó libre de prerrequisitos! Lo metemos a la cola
                }
            }
        }
        
        // 3. Si completamos todos los cursos, no hubo ciclos
        return completed == numCourses;
    }
}