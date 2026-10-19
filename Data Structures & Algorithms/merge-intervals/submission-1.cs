public class Solution {
    public int[][] Merge(int[][] intervals) {
        if (intervals == null || intervals.Length <= 1) return intervals;

        // Sort by the start of each interval
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));

        List<int[]> merged = new List<int[]>();

        foreach (int[] current in intervals) {
            if (merged.Count == 0) {
                merged.Add((int[])current.Clone());
            } else {
                int[] last = merged[merged.Count - 1];
                // No overlap: current starts after the last merged ends
                if (current[0] > last[1]) {
                    merged.Add((int[])current.Clone());
                } else {
                    // Overlap: extend the end of the last merged interval
                    last[1] = Math.Max(last[1], current[1]);
                }
            }
        }

        return merged.ToArray();
    }
}