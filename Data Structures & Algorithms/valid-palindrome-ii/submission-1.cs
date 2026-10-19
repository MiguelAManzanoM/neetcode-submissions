public class Solution {
    public bool ValidPalindrome(string s) {
        bool checkPalindrome(string s, int i, int j) {
            while (i < j) {
                if (s[i] != s[j]) {
                    return false;
                }
                i++;
                j--;
            }
            return true;
        }
        int left = 0;
        int right = s.Length - 1;

        while (left < right) {
            if (s[left] != s[right]) {
                return (checkPalindrome(s, left + 1, right) 
                || checkPalindrome(s, left, right - 1));
            }
            left++;
            right--;
        }
        return true;
    }
}