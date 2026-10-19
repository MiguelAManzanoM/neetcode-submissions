public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        Dictionary<char, int> count = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++) {
            if (!count.ContainsKey(s[i]))
                count[s[i]] = 0;
            count[s[i]]++;
            
            if (!count.ContainsKey(t[i]))
                count[t[i]] = 0;
            count[t[i]]--;
        }

        foreach ((char letter, int letterCount) in count) {
            if (letterCount != 0) return false;
        }
        return true;
    }
}
