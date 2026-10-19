public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if (strs == null || strs.Length == 0) {
            return "";
        }

        for (int i = 0; i < strs[0].Length; i++) {
            
            foreach (string str in strs) {
                if (i == str.Length || str[i] != strs[0][i]) {
                    return str.Substring(0, i);
                }
            }
        }

        return strs[0];
    }
}