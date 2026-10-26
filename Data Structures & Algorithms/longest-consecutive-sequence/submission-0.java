class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        else if (n == 1) {
            return 1;
        }
        HashSet<Integer> unique = new HashSet<Integer>();
        for (int num : nums) {
            unique.add(num);
        }
        int longestSequence = 1;
        for (int num : nums) {
            if (!unique.contains(num - 1)) {
                int currentNum = num;
                int currentSequence = 1;
                while (unique.contains(currentNum + 1)) {
                    currentNum++;
                    currentSequence++;
                }
                longestSequence = Math.max(longestSequence, currentSequence);
            }
        }
        return longestSequence;
    }
}
